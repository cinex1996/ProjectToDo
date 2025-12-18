from pyexpat.errors import messages

from flask import request, render_template

from app.blueprints.search import bp
from app.models.users import User


@bp.route("/search_user",methods=["GET","POST"])
def search_user():
    message, email = None, None

    if request.method == "POST":
        search = request.form.get("search").strip() or ""

        if not search:
            message = "Podaj email użytkownika"
        else:
            email = User.query.filter_by(email=search).first()
            if email:
                message = "Taki użytkownik istnieje"
            else:
                message = "Taki użytkownik nie istnieje"

    return render_template("tasks/search_user.html", message=message,email=email)