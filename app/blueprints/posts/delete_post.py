from flask import request, redirect, url_for, flash, render_template, session

from app import db
from app.blueprints.posts import bp
from app.models.posts import Post

@bp.route('/delete/<int:id>', methods=['POST'])
def delete_post(id):
    post = Post.query.get(id)

    if not post:
        flash('Post does not exist')
        return redirect(url_for('main.home'))

    if post.user_id != session.get('user_id'):
        flash('You cannot delete this post')
        return redirect(url_for('main.home'))


    db.session.delete(post)
    db.session.commit()

    flash('Post usunięty', 'success')

    return redirect(url_for('main.home'))