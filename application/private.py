import os

from flask import Blueprint
from application.sitemap import sitemapper
from application.utils import get_lastmod_date, render_page

path = os.path.split(os.path.abspath(__file__))[0] + "/private/"

bp = Blueprint("private", __name__)

fl = [x[0][len("application/private/"):] for x in os.walk("application/private/")][1:]

@sitemapper.include(url_variables={"name": fl}, lastmod=[get_lastmod_date(f, path) for f in fl])
@bp.route("/private/<path:name>/")
def show_page(name):
    return render_page( path + name + "/", path)

