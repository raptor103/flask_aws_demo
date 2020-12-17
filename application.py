"""
Runs Flask app.
"""

from flask import Flask
application = Flask(__name__)

@application.route('/')
def greetings():
    """
    Greetings
    """
    return 'Made it to AWS?'

if __name__ == "__main__":
    application.run()
