#!/usr/bin/python3
"""
<<<<<<< HEAD
starts a Flask web application
"""

from flask import Flask
=======
A simple flask server running on 0.0.0.0:5000
"""
from flask import Flask

>>>>>>> d364182adf6b6aebc07fd37d00692d0bd7608f44
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
def display():
    """Prints 'Hello HBNB!' to display"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> d364182adf6b6aebc07fd37d00692d0bd7608f44
