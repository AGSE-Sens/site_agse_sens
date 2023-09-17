import os

from flask import Blueprint
from application.sitemap import sitemapper
from application.utils import get_lastmod_date, render_page

path = os.path.split(os.path.abspath(__file__))[0] + "/pages/"

bp = Blueprint("page", __name__)

@sitemapper.include(lastmod=get_lastmod_date("accueil", path))
@bp.route("/")
def accueil():
    return render_page( path + "accueil" + "/", path)

fl = [x[0][len("application/pages/"):] for x in os.walk("application/pages/")][1:]

@sitemapper.include(url_variables={"name": fl}, lastmod=[get_lastmod_date(f, path) for f in fl])
@bp.route("/page/<path:name>/")
def show_page(name):
    return render_page( path + name + "/", path)
