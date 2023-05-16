from flask import Flask
from flask import Blueprint
from flask import redirect
from flask import render_template
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
    "superscript",
    "subscript",
    "markdown_checklist.extension",
    "markdown_del_ins",
    "markdown_mark",
    "mdx_unimoji",
]

import shutil, os
path = os.path.split(os.path.abspath(__file__))[0] + "/"
shutil.copyfile(path + "init.py", path + "src/__init__.py")

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


page.dirlist.remove("accueil")

for i in page.dirlist:
    exec(
        f"""\
@bp.route("/{i}")
def {i}_page():
    return render_module({i})"""
    )
