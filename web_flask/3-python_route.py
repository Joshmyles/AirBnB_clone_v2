#!/usr/bin/python3

"""script that starts a flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """prints Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    prints HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """display C followed by value of the text
    replace underscore symbols with a space
    """
    return "C " + text.replace("_", " ")


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """
    display Python followed by value of the text 
    replace underscore with a space
    """
    return "Python " + text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
