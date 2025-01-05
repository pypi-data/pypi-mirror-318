"""About page."""

from flask import Blueprint, render_template

# pylint: disable=missing-function-docstring

# about_bp = Blueprint("about", __name__)
about_bp = Blueprint(
    "about",
    __name__,
    template_folder="templates/about",
    static_folder="static/about",
    static_url_path="/static/about"
)

@about_bp.route("", methods=["GET"])
def view_about():

    return render_template("about.html")
