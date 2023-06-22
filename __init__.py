import os

from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask_inflate import Inflate
from flask_minify import Minify

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
    )
    try :
        with open("key.txt","r") as file:
            app.config.from_mapping(
                # a default secret that should be overridden by instance config
                SECRET_KEY=file.read(),
            )
    except :
        print(
"""***************************************************
                !!! No key set !!!
***************************************************""")

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(403, forbiden)

    app.config.from_pyfile("config.py", silent=True)

    inf = Inflate()
    inf.init_app(app)
    Minify(app=app)

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    @app.route("/favicon.ico")
    def favicon():
        return send_from_directory(
            os.path.join(app.root_path, "static"),
            "favicon.ico",
            mimetype="image/vnd.microsoft.icon",
        )

    @app.route("/robots.txt")
    def robot():
        return send_from_directory(
            os.path.join(app.root_path, "static"),
            "robots.txt",
            mimetype="text/plain",
        )

    # apply the blueprints to the app

    from site_agse_sens import page
    app.register_blueprint(page.bp)

    from site_agse_sens import admin
    app.register_blueprint(admin.bp)

    return app
