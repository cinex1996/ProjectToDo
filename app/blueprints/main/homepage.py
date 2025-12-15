from flask import render_template, session
from . import bp
from ...decorators import login_requirement, nocache
from app.models.Posts import Post



@login_requirement
@nocache
@bp.route("/homepage",methods=["GET"])
def home():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template("tasks/index.html", posts=posts)
