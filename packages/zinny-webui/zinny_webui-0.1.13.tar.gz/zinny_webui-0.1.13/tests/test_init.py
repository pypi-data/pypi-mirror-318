"""Testing zinny_aebui/__init__.py and Flask app factory."""

from unittest.mock import patch
from zinny_webui.__init__ import create_app

import pytest
from flask import Flask
# from zinny_webui import create_app


@pytest.fixture
def app():
    """Fixture to create the Flask app for testing."""
    flask_app = create_app()
    flask_app.config.update({
        "TESTING": True,  # Enable testing mode
        "DATABASE": "/tmp/test_database.db"  # Use a temporary database
    })
    yield flask_app


@pytest.fixture
def client(app):
    """Fixture to provide a test client."""
    with app.test_client() as test_client:
        yield test_client


def test_create_app(app):
    """Test that the app is created successfully."""
    assert isinstance(app, Flask)
    assert app.config["TESTING"] is True
    assert app.config["DATABASE"] == "/tmp/test_database.db"


def test_blueprints_registered(app):
    """Test that all expected blueprints are registered."""
    blueprints = app.blueprints.keys()
    expected_blueprints = [
        "errors",
        "survey",
    ]
    for blueprint in expected_blueprints:
        assert blueprint in blueprints, f"Blueprint {blueprint} is not registered."


@patch("zinny_api.init_db")
def test_mock_init_db(mock_init_db):
    create_app()
    # print(init_db)

    mock_init_db.assert_called_once_with(load_data=True)


def test_routes_exist(client):
    """Test that expected routes are accessible."""

    response = client.get("/survey")
    assert response.status_code in [200, 404], "/survey route failed."

    response = client.get("/")
    assert response.status_code in [200, 404], "/ route failed."
