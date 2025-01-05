from flask import Blueprint, render_template

survey_bp = Blueprint('survey', __name__)


# survey_bp = Blueprint(
#     'survey',
#     __name__,
#     static_folder="static",
#     static_url_path="/static"
# )


@survey_bp.route('/component/')
def survey_component():
    return render_template('surveys/survey_component.html')


@survey_bp.route('/')
def survey_page():
    return render_template('surveys/survey_page.html')
