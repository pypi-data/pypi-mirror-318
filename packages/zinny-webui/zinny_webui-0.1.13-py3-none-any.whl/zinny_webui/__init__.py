"""Main application file for the Zinny Flask server."""
import os
import importlib

from flask import Flask
from .routes.errors import errors_bp
from .views.survey import survey_bp
from .views.about import about_bp
from .config import ZINNY_API_VERSION, ZINNY_WEBUI_VERSION


# pylint: disable=import-outside-toplevel,line-too-long


# Application Factory
def create_app():
    """Init the Web UI."""
    import zinny_api
    # app = Flask(__name__)
    flask_app = zinny_api.create_app()

    # Resolve paths relative to this file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_folder = importlib.resources.files("zinny_webui").joinpath("static")
    template_folder = importlib.resources.files("zinny_webui").joinpath("templates")

    # Update static folder configuration for zinny_webui
    flask_app.static_url_path = "/static"
    flask_app.static_folder = str(static_folder)
    flask_app.template_folder = str(template_folder)
    flask_app.config["WEBUI_TITLE"] = "Zinny WebUI"

    # Retrieve and inject version numbers
    flask_app.config["ZINNY_API_VERSION"] = ZINNY_API_VERSION
    flask_app.config["ZINNY_WEBUI_VERSION"] = ZINNY_WEBUI_VERSION

    # # Debug prints
    # print("CWD:", os.getcwd())
    # print("App root path:", flask_app.root_path)
    # print("Static folder:", flask_app.static_folder)
    # print("Template folder:", flask_app.template_folder)
    # print("Static URL path:", flask_app.static_url_path)

    # Import blueprints
    flask_app.register_blueprint(survey_bp)  # Root route, no prefix
    flask_app.register_blueprint(errors_bp)
    flask_app.register_blueprint(about_bp, url_prefix='/about')

    return flask_app
