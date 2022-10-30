#!/usr/bin/python3
"""
<<<<<<< HEAD
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
A simple flask server running on 0.0.0.0:5000
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def display_root():
    """Prints 'Hello HBNB!' to display"""
    return "Hello HBNB!"


@app.route('/hbnb')
def display_hbnb():
    """Prints 'HBNB' to display"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/')
@app.route('/python/<text>')
def display_python(text="is cool"):
    """Print route param to display"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
>>>>>>> d364182adf6b6aebc07fd37d00692d0bd7608f44
