from flask import Flask
from flask import Blueprint
from flask import redirect
from flask import render_template
from werkzeug.exceptions import abort

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("main/index.html")
