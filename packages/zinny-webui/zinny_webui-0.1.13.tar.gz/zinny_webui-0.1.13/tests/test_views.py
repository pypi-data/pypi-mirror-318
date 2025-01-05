"""Testing views (UI)"""
import os
from unittest.mock import patch
import pytest
import json

from zinny_webui.__init__ import create_app

from zinny_api.db.db_init import get_connection
from zinny_api.db.db_schema import SCHEMA_TITLES_TABLE, SCHEMA_SURVEYS_TABLE
from .data_samples import SURVEY_VFX_SAMPLE, SURVEY_PICTURE_SAMPLE
from .util_db_helpers import add_surveys_test_data

# pylint: disable=redefined-outer-name,line-too-long
# pylint: disable=missing-function-docstring,unused-argument

@pytest.fixture(scope="function")
def setup_database(monkeypatch):
    test_db_path = "/tmp/test_database.db"

    monkeypatch.setattr("zinny_api.db.db_init.DATABASE_PATH", test_db_path)
    # monkeypatch.setattr("zinny_api.db.db_init.DATABASE_PATH", "sqlite:///:memory:")
    conn = get_connection()
    yield conn
    conn.close()


@pytest.fixture
def app():
    """Fixture to create the Flask app for testing."""
    flask_app = create_app()
    flask_app.config.update({
        "TESTING": True,  # Enable testing mode
        "DATABASE": "/tmp/test_database.db"  # Use a temporary database
    })
    yield flask_app


# @pytest.fixture(scope="function")
# def setup_database(monkeypatch):
#     """Set up a fresh database for each test."""
#     test_db_path = "/tmp/test_database.db"
#     monkeypatch.setattr("zinny_api.db.DATABASE_PATH", test_db_path)

#     schema = SCHEMA_TITLES_TABLE + SCHEMA_SURVEYS_TABLE

#     conn = get_connection()
#     with conn:
#         conn.executescript(schema)
#         print("Inserting sample data...")
#         # Insert shared survey data
#         add_surveys_test_data(conn, [SURVEY_VFX_SAMPLE, SURVEY_PICTURE_SAMPLE])
#         conn.commit()
#     conn.close()

#     yield

#     if os.path.exists(test_db_path):
#         os.remove(test_db_path)


@pytest.fixture
def client(setup_database):
    # pylint: disable=import-outside-toplevel
    from flask import Flask
    # from zinny_webui.views.title import title_bp
    # from zinny_webui.views.rate import rate_bp
    from zinny_webui.views.about import about_bp

    # app = Flask(__name__, template_folder="app/templates")  # Set the template folder path
    template_folder = os.path.abspath("zinny_webui/templates")
    app = Flask(__name__, template_folder=template_folder)
    # template_folder = os.path.join(current_app.root_path, "templates")
    # app = Flask(__name__, template_folder=template_folder)

    # app.register_blueprint(title_bp, url_prefix='/title')
    # app.register_blueprint(rate_bp, url_prefix='/rate')
    app.register_blueprint(about_bp, url_prefix='/about')

    with app.test_client() as client:
        yield client


# def test_view_title(client):
#     """Test the /title/view/<title_id> endpoint."""

#     response = client.get('/title/view/1')
#     assert response.status_code == 200
#     assert b"Sample Movie" in response.data
#     assert b"2000" in response.data

#     response = client.get('/title/view/999')
#     assert response.status_code == 404
#     assert b"404" in response.data



def test_404_page(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404
    assert b"Not Found" in response.data
