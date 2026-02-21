from flask import request, redirect, url_for, flash, render_template, session

from app import db
from app.blueprints.posts import bp
from app.models.posts import Post
from sqlalchemy.orm.sync import update


@bp.route('edit_post/<int:post_id>',methods=["GET", "POST"])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)

    # sprawdzacsz czy post nalezy do zalogowane uzytkwonika
    if post.user_id != session.get('user_id'):
        flash("To nie jest twój post")
        return redirect(url_for('main.home'))
    if request.method == "POST":
        updated_post = request.form.get("Post", "").strip()

        if not updated_post:
            return redirect(url_for('main.home'))
        post.post = updated_post
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template("tasks/edit_post.html")
