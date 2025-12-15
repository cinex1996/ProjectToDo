from flask import request, redirect, url_for, flash, render_template, session

from app import db
from app.blueprints.posts import bp
from app.models.Posts import Post


@bp.route("/create_post", methods=["POST","GET"])
def create_post():
    if request.method == "POST":
        current_post = request.form.get("Post","").strip()
        if not current_post:
            flash("Musisz uzupełnić pole jak chcesz dodać post","error")
            return render_template("tasks/index.html")
        user_id=session.get("user_id")
        if current_post:
            new_post = Post(post=current_post, category="Status", user_id=user_id)
            db.session.add(new_post)
            db.session.commit()
            flash("Dodałeś post", "success")
            return redirect(url_for("main.home"))
