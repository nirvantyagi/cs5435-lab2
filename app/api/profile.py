from bottle import (
    abort,
    get,
    post,
    request,
    jinja2_template as template,
)

from app.models.session import logged_in
from app.models.user import get_user

@get("/profile/<username:path>")
@logged_in
def profile(db, session, username):
    user = get_user(db, username)
    session_user = get_user(db, session.get_username())
    if user is None:
        return template(
            "profile",
            user=session_user,
            session_user=session_user,
            error="User {} does not exist".format(username)
        )
    return template(
        "profile",
        user=user,
        session_user=session_user,
    )

@post('/aboutme')
@logged_in
def update_aboutme(db, session):
    user = get_user(db, session.get_username())
    aboutme = request.forms.get('aboutme')
    user.update_aboutme(aboutme)
    return template(
        "profile",
        user=user,
        session_user=user,
    )

