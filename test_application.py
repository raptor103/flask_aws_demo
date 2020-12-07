import requests
from flask import jsonify

def test_greetings(url='http://localhost:5000'):
    response = requests.get(url)
    assert response.status_code == 200
test_greetings()
