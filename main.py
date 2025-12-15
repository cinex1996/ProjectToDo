import sys; print("PYTHON RUNTIME:", sys.executable)
from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
print("STATIC", app.static_folder)
print("TEMPLATES", app.template_folder)

if __name__ == "__main__":
    app.run(debug=True,port=4000,host="0.0.0.0")