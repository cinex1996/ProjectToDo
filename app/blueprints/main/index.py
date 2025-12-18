from flask import render_template, request
from . import bp

@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("tasks/homepage.html")
    return render_template("tasks/index.html")
