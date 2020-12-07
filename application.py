from flask import Flask
application = Flask(__name__)

@application.route('/')
def greetings():
    """
    Greetings
    """
    return 'Ahoj, jak se máš?'

if __name__ == "__main__":
    application.run()
