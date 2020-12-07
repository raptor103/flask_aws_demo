"""
Tests Flask app
"""

def test_application(client):
    """
    Tests flask application
    """
    res = client.get('/')
    assert res.status_code == 200
