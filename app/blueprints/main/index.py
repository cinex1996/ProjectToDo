from flask import render_template, request, redirect, url_for, flash, session, current_app
from sqlalchemy import func
from . import bp
from werkzeug.security import check_password_hash
from app.models.users import User

@bp.route("/", methods=["GET", "POST"])
def index():
    # GET: jeśli zalogowany -> na home
    if request.method == "GET":
        return render_template("tasks/homepage.html")
    return render_template("tasks/index.html")
