from flask import Flask
from flask import Blueprint
from flask import redirect
from flask import render_template
from werkzeug.exceptions import abort

import site_agse_sens.src.vert as vert
import site_agse_sens.src.jaune as jaune
import site_agse_sens.src.rouge as rouge
import site_agse_sens.src.accueil as accueil

bp = Blueprint("main", __name__)


def render_module(path, filelist, title="", subtitle="", page_title="", description=""):
    return render_template(
        "main/blob.html",
        filelist=[
            ["md" if i[-3:] == ".md" else "html", open(path + i, "r").read()]
            for i in filelist
        ],
        title=title,
        subtitle=subtitle,
        page_title=page_title,
        description=description,
    )


@bp.route("/")
def index():
    return render_module(
        accueil.path,
        accueil.filelist,
        title=accueil.title,
        subtitle=accueil.subtitle,
        page_title="Accueil",
        description=accueil.description,
    )


@bp.route("/vert")
def branche_verte():
    return render_module(
        vert.path,
        vert.filelist,
        title=vert.title,
        subtitle=vert.subtitle,
        page_title="Branche Verte",
        description=vert.description,
    )

@bp.route("/jaune")
def branche_jaune():
    return render_module(
        jaune.path,
        jaune.filelist,
        title=jaune.title,
        subtitle=jaune.subtitle,
        page_title="Branche jaune",
        description=jaune.description,
    )

@bp.route("/rouge")
def branche_rouge():
    return render_module(
        rouge.path,
        rouge.filelist,
        title=rouge.title,
        subtitle=rouge.subtitle,
        page_title="Branche rouge",
        description=rouge.description,
    )
