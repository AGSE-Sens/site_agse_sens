from flask import Flask
from flask import Blueprint
from flask import redirect
from flask import render_template
from werkzeug.exceptions import abort

import site_agse_sens.src.vert as vert

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("main/index.html")


@bp.route("/blob/vert")
def blob():
    return render_template(
        "main/blob.html",
        filelist=[
            ["md" if i[-3:] == ".md" else "html", open(vert.path + "/" + i, "r").read()]
            for i in vert.filelist
        ],
        title="Hello, world!",
        subtitle="Ceci est un test",
    )
