from functools import wraps
from flask import session, redirect, url_for, request, flash, make_response

def login_requirement(view_func): # TODO login_required
    @wraps(view_func)
    def wrapper(*args,**kwargs):
        if "user_id" not in session:
            next_url=request.path
            flash("Zaloguj się, aby zobaczyć tę stronę", "warning")
            return redirect(url_for("main.index", next=next_url))
        return view_func(*args, **kwargs)

    return wrapper

def nocache(view):
    @wraps(view)
    def wrapper(*args,**kwargs):
        resp = make_response(view(*args,**kwargs))
        resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0, private"
        resp.headers["Pragma"] = "no-cache"
        resp.headers["Expires"] = "0"
        return resp
    return wrapper
