import pytest
from application import application as flask_app

# This file will initialize our Flask app

@pytest.fixture
def application():
    yield flask_app


@pytest.fixture
def client(application):
    return application.test_client()
