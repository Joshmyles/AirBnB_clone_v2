#!/usr/bin/python3

"""script that starts a flask web application

web application must be listening on 0.0.0.0, port 5000
routes:
/ - display Hello HBNB
/hbnb - display HBNB
/c/<text> - display c followed by the value of the text, replace underscore with a space
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text():
    """displays C followed by the value of the text variable
    Replace underscore _ with a space
    """
    return "C " + text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
