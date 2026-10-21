from functools import wraps

from flask import flash, redirect, session


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("You must be logged in to do this!")
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function
