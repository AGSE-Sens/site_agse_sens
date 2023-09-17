import os

from flask import Blueprint
from flask import redirect
from flask import request
from flask import flash
from flask import session
from flask import url_for
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from application.utils import get_lastmod_date, render_page, login_required

path = os.path.split(os.path.abspath(__file__))[0] + "/private/"

bp = Blueprint("private", __name__)

fl = [x[0][len("application/private/"):] for x in os.walk("application/private/")][1:]

@bp.route("/private/<path:name>/")
@login_required
def show_page(name):
    return render_page( path + name + "/", path)

@bp.route("/private/login/", methods=("GET", "POST"))
def login():
    """Log in a user by setting session key 'logged' to True."""

    if request.method == "POST":
        password = request.form["password"]
        error = None
        hashpswd = ""
        try :
            with open("hash.txt","r") as file:
                hashpswd = file.read()
        except :
            error = "Fonctionnalité non disponible"

        if not check_password_hash(hashpswd, password):
            if error == None:
                session.clear()
                error = "Mot de passe incorrect"

        if error == None:
            session.clear()
            session["logged"] = True
            flash("Connexion réussie")
            if request.args.get("name") != None :
                return redirect(url_for("private.show_page", name=request.args.get("name")))
            return redirect(url_for("page.accueil"))

        flash(error)
    return render_page( path + "login" + "/", path)
