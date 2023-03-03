from flask import Flask
from flask import Blueprint
from flask import redirect
from flask import render_template
from werkzeug.exceptions import abort

import markdown

md_extensions = [
    "extra",
    "abbr",
    "attr_list",
    "def_list",
    "fenced_code",
    "footnotes",
    "tables",
    "admonition",
    "codehilite",
    "legacy_attrs",
    "legacy_em",
    "meta",
    "nl2br",
    "sane_lists",
    "smarty",
    "toc",
    "wikilinks",
    "superscript",
    "subscript",
    "markdown_checklist.extension",
    "markdown_del_ins",
]

import site_agse_sens.src as page

for i in page.dirlist:
    exec("import site_agse_sens.src." + i + " as " + i)

bp = Blueprint("main", __name__)


def render_module(module):
    return render_template(
        "main/blob.html",
        filelist=[
            [
                "md" if i[-3:] == ".md" else "html",
                markdown.markdown(
                    open(module.path + i, "r").read(),
                    extensions=md_extensions,
                )
                if i[-3:] == ".md"
                else open(module.path + i, "r").read(),
            ]
            for i in module.filelist
        ],
        title=module.title,
        subtitle=module.subtitle,
        page_title=module.page_title,
        description=module.description,
        use_head=module.use_head,
    )


@bp.route("/")
def index():
    return render_module(accueil)


@bp.route("/vert")
def branche_verte():
    return render_module(vert)


@bp.route("/jaune")
def branche_jaune():
    return render_module(jaune)


@bp.route("/rouge")
def branche_rouge():
    return render_module(rouge)


@bp.route("/contact")
def contact_page():
    return render_module(contact)


@bp.route("/instructions")
def instructions_page():
    return render_module(instructions)
