#!/usr/bin/python3
'''
- A python script that starts a Flask web application.
- The web application listens on 0.0.0.0, port 5000
- Route '/' displays "Hello HBNB!".

Usage:
    python3 -m web_flask.0-hello_route
    In another tab:  curl 0.0.0.0:5000 ; echo "" | cat -e
'''
from flask import Flask

''' Creates a Flask application instance'''
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def call_hbnb():
    '''Function  displays "Hello HBNB!" on running the URL'''

    return "Hello HBNB!"


if __name__ == "__main__":

    ''' Running the  Flask appllication'''
    app.run(host='0.0.0.0', port='5000')
