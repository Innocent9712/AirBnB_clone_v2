#!/usr/bin/python3
"""
A simple flask server running on 0.0.0.0:5000
"""
from flask import Flask, render_template

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


@app.route('/number/<int:n>')
def display_n(n):
    """Print n if n is int"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def display_n_template(n):
    """Return an html page with value of n"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def diplay_n_odd_or_even(n):
    """Return html page with if n is odd or even"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
