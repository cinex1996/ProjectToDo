from sys import prefix

from flask import Flask


from .extensions import db, migrate, csrf
from .config import Config

def create_app(config_object: type[Config] = Config) -> Flask:
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(config_object)

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # Importy zależne od app/db – dopiero tutaj:
    from .blueprints.main import bp as main_bp
    from .blueprints.auth import bp as auth_bp
    from .blueprints.reset import bp as reset_bp
    from .blueprints.posts import bp as create_bp
    app.register_blueprint(main_bp, url_prefix="/")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(reset_bp, url_prefix="/reset")
    app.register_blueprint(create_bp, url_prefix="/posts")

    @app.after_request
    def secure_headers(resp):
        resp.headers.setdefault("X-Content-Type-Options", "nosniff")
        resp.headers.setdefault("X-Frame-Options", "DENY")
        resp.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        resp.headers.setdefault("Content-Security-Policy", "default-src 'self'; img-src 'self' data:")
        return resp

    return app