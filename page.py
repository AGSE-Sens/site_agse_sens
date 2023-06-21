import os

from flask import Flask
from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import abort
from werkzeug.exceptions import abort

import markdown

md_extensions = [
    "extra",
    "legacy_attrs",
    "legacy_em",
    "meta",
    "nl2br",
    "sane_lists",
    "toc",
    "wikilinks",
    # "superscript",
    # "subscript",
    # "markdown_checklist.extension",
    # "markdown_del_ins",
    # "markdown_mark",
    # "mdx_unimoji",
]

path = os.path.split(os.path.abspath(__file__))[0] + "/src/"

bp = Blueprint("page", __name__)


def render_page(page_path):
    if os.path.exists(page_path) == False :
        abort(404)
    filelist = sorted([i for i in os.listdir(page_path) if os.path.splitext(page_path+i)[1] in [".md",".html"]])
    title = ""
    subtitle = ""
    page_title = page_path.split("/")[-1]
    description = ""
    use_head = True
    title = ""
    try :
        with open(page_path + "TITLE", "r") as f:
            title = f.readline().rstrip()
            subtitle = [i.rstrip() for i in f.readlines()]
    except FileNotFoundError :
        use_head = False

    try :
        with open(page_path + "DESCRIPTION", "r") as f:
            description = f.read().rstrip()
    except FileNotFoundError :
        pass

    try :
        with open(page_path + "NAME", "r") as f:
            page_title = f.read().rstrip()
    except FileNotFoundError :
        pass

    return render_template(
        "main/blob.html",
        filelist=[
            [
                os.path.splitext(page_path+i)[1][1:],
                markdown.markdown(
                    open(page_path + i, "r").read(),
                    extensions=md_extensions,
                )
                if os.path.splitext(page_path+i)[1] == ".md"
                else open(page_path + i, "r").read(),
            ]
            for i in filelist
        ],
        title=title,
        subtitle=subtitle,
        page_title=page_title,
        description=description,
        use_head=use_head,
    )


@bp.route("/")
def accueil():
    return render_page( path + "accueil" + "/")


@bp.route("/page/<path:name>")
def show_page(name):
    return render_page( path + name + "/")
