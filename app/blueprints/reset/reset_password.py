from flask import render_template, request, redirect, url_for, flash
from app.blueprints.reset import bp
from ...extensions import db
from app.models.users import User
from werkzeug.security import generate_password_hash


@bp.route("/reset_password", methods=["GET","POST"])  # /reset
def reset_password():
    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        password = request.form.get("PasswordForgot") or ""
        password_repeat = request.form.get("RepeatPassword") or ""

        if not email or not password or not password_repeat:
            flash("Wszystkie pola muszą być uzupełnione","error")
            return redirect(url_for("reset.forgot"))

        if password != password_repeat:
            flash("Hasła muszą być takie same","error")
            return redirect(url_for("reset.forgot"))

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("Taki użytkownik nie istnieje","error")
            return redirect(url_for("reset.forgot"))

        user.password_hash = generate_password_hash(password)
        db.session.commit()

        flash("Hasło zostało zmienione","success")

        return redirect(url_for("main.index"))
    return render_template("tasks/reset_password.html")