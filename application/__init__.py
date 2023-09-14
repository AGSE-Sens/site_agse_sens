import os

from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask_inflate import Inflate
from flask_compress import Compress
from flask_minify import Minify
from application.sitemap import sitemapper

def page_not_found(e):
    return render_template("404.html"), 404

def forbiden(e):
    return render_template("403.html", erreur=e), 403

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(
        __name__,
        static_url_path="",
        static_folder="static",
    )
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY=os.urandom(40),
        PREFERRED_URL_SCHEME="https",
    )

    try:
        with open("key.txt", "rb") as keyfile:
            app.config.from_mapping(
                SECRET_KEY=keyfile.read(),
            )
    except:
        print(
            """***************************************************
               !!! No key found !!!
***************************************************"""
        )
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(403, forbiden)

    app.config.from_pyfile("config.py", silent=True)

    inf = Inflate()
    inf.init_app(app)
    compress = Compress()
    compress.init_app(app)
    Minify(
        app=app,
        caching_limit=12,
        )

    @app.route("/hello/")
    def hello():
        return "Hello, World!"

    @app.route("/robots.txt")
    def robot():
        return send_from_directory(
            os.path.join(app.root_path, "static"),
            "robots.txt",
            mimetype="text/plain",
        )

    @app.route("/404/")
    @app.route("/404.html")
    def page_not_found_no_error():
        return render_template("404.html")

    @app.route("/sitemap.xml")
    def r_sitemap():
        return sitemapper.generate(gzip=True)

    # apply the blueprints to the app

    from application import page
    from application import private

    app.register_blueprint(page.bp)
    app.register_blueprint(private.bp)

    sitemapper.init_app(app)

    return app


if __name__ == "__main__":
    create_app()
