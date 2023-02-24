from flask import Flask
from flask import Blueprint
from flask import redirect
from flask import render_template
from werkzeug.exceptions import abort

import site_agse_sens.src.vert as vert
import site_agse_sens.src.jaune as jaune
import site_agse_sens.src.rouge as rouge
import site_agse_sens.src.accueil as accueil
import site_agse_sens.src.contact as contact
import site_agse_sens.src.instructions as instructions

bp = Blueprint("main", __name__)


def render_module(
    path,
    filelist,
    title="",
    subtitle="",
    page_title="",
    description="",
    use_head=True,
):
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
        use_head=use_head,
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


@bp.route("/contact")
def contact_page():
    return render_module(
        contact.path,
        contact.filelist,
        page_title="Contact",
        description=contact.description,
        use_head=False,
    )

@bp.route("/instructions")
def instructions_page():
    return render_module(
        instructions.path,
        instructions.filelist,
        page_title="Instructions",
        use_head=False,
    )
