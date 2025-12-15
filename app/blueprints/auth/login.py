from flask import request, flash, redirect, url_for, session, render_template
from sqlalchemy import func
from werkzeug.security import check_password_hash

from app.blueprints.auth import bp
from app.models.users import User
@bp.route("/login", methods=["GET", "POST"])
def login():
    # Jeśli użytkownik już zalogowany, nie pokazuj mu formularza
    if session.get("user_id") and request.method == "GET":
        flash("Jesteś już zalogowany.", "info")
        return redirect(url_for("main.home"), code=302)

    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        password = request.form.get("password") or ""

        if not email or not password:
            flash("Wszystkie pola muszą być uzupełnione", "error")
            return redirect(url_for("auth.login"), code=303)

        user = User.query.filter(func.lower(User.email) == email).first()

        if not (user and user.password_hash and check_password_hash(user.password_hash, password)):
            # Na wszelki wypadek czyścimy sesję, żeby stare zalogowanie nie mieszało
            session.clear()
            flash("Nieprawidłowy email lub hasło", "error")
            return redirect(url_for("auth.login"), code=303)

        # Sukces logowania
        session.clear()
        session["user_id"] = user.id
        session["email"] = user.email
        flash("Zalogowano pomyślnie!", "success")
        return redirect(url_for("main.home"), code=303)

    # GET – pierwszy raz / form po przekierowaniu
    return render_template("tasks/homepage.html")

