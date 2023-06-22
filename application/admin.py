from flask import Flask
from flask import Blueprint
from flask import redirect
from flask import url_for
from flask import render_template
from flask import abort
from flask import request
from flask import flash
from flask import session
from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from werkzeug.exceptions import BadRequestKeyError
import functools

bp = Blueprint("admin", __name__)

@bp.route("/admin/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        password = request.form["password"]
        error = ""
        adminpswd = ""
        try :
            with open("admin.txt","r") as file:
                adminpswd = file.read()
        except :
            error += "Mot de passe Administrateur non renseigné"

        if not check_password_hash(adminpswd, password):
            if error == "":
                error = "Mot de passe incorrect"

        if error == "":
            session.clear()
            session["user_id"] = 1
            flash("Vous avez été connecté en tant qu'administrateur.")
            return redirect(url_for("admin.admin"))

        flash(error)
    return render_template("admin/login.html")

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get("user_id") != 1:
            return redirect(url_for("admin.login"))
        return view(**kwargs)
    return wrapped_view

@bp.route("/admin", methods=("GET", "POST"))
@login_required
def admin():
    return render_template("admin/admin.html")

@bp.route("/admin/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("admin.login"))
