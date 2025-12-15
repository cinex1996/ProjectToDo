from flask import redirect, url_for, session, flash
from . import bp

@bp.route("/logout",methods=["POST","GET"])
def logout():
    session.clear()
    flash("Wylogowano.", "info")
    return redirect(url_for("main.index"),code=303)
