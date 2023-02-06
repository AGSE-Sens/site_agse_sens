import os

from flask import Flask
from flask import render_template
from flask import send_from_directory
from flaskext.markdown import Markdown
from flask_inflate import Inflate


def page_not_found(e):
    return render_template("404.html"), 404


def forbiden(e):
    return render_template("403.html", erreur=e), 403


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_url_path="",
        static_folder="static",
    )
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(403, forbiden)

    app.config.from_pyfile("config.py", silent=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    Markdown(app)
    inf = Inflate()
    inf.init_app(app)

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

    # apply the blueprints to the app

    from site_agse_sens import main

    app.register_blueprint(main.bp)

    app.add_url_rule("/", endpoint="index")

    return app
