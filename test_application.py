import requests
from flask import jsonify

def test_application(application, client):
    """
    Tests flask application
    """
    res = client.get('/')
    assert res.status_code == 200
