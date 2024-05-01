#!/usr/bin/python3
'''
- A python script that starts a Flask web application.
- The web application listens on 0.0.0.0, port 5000
- Route '/' displays "Hello HBNB!".

Usage:
    python3 -m web_flask.2-c_route
    In another tab:  curl 0.0.0.0:5000/c/is_fun  ; echo "" | cat -e
'''
from flask import Flask

''' Creates a Flask application instance'''
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def call_hbnb():
    '''Function  displays "Hello HBNB!" on running the URL'''

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def call_HBNB():
    '''Function displays "HBNB" on running the URL'''

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def call_c_text(text):
    '''Function displays "C <followed by the text value>"'''

    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":

    ''' Running the  Flask application'''
    app.run(host='0.0.0.0', port='5000', debug=True)
