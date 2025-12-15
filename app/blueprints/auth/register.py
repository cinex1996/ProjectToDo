from flask import render_template, request, redirect, url_for, flash
from . import bp
from ...extensions import db
from app.models.users import User
from werkzeug.security import generate_password_hash

@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        password = request.form.get("password") or ""
        password_repeat = request.form.get("PasswordRepeat") or "" # TODO password_repeat

        if not email or not password or not password_repeat:
            flash("Wszystkie pola muszą być uzupełnione","error")
            return redirect(url_for("auth.register"))

        if password != password_repeat:
            flash("Hasła muszą być takie same","error")
            return redirect(url_for("auth.register"))

        if User.query.filter_by(email=email).first():
            flash("Użytkownik z tym emailem już istnieje","warning")
            return redirect(url_for("auth.register"))

        user = User(email=email, password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        flash("Konto utworzone. Zaloguj się.","success")

        return redirect(url_for("main.index"))

    return render_template("tasks/register.html")