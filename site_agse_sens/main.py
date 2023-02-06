from flask import Flask
from flask import Blueprint
from flask import redirect
from flask import render_template
from werkzeug.exceptions import abort

import site_agse_sens.src.vert as vert
import site_agse_sens.src.accueil as accueil

bp = Blueprint("main", __name__)


def render_module(path, filelist, title="", subtitle=""):
    return render_template(
        "main/blob.html",
        filelist=[
            ["md" if i[-3:] == ".md" else "html", open(path + i, "r").read()]
            for i in filelist
        ],
        title=title,
        subtitle=subtitle,
    )


@bp.route("/")
def index():
    return render_module(
        accueil.path, accueil.filelist, title=accueil.title, subtitle=accueil.subtitle
    )


@bp.route("/blob/vert")
def blob():
    return render_module(
        vert.path, vert.filelist, title=vert.title, subtitle=vert.subtitle
    )
