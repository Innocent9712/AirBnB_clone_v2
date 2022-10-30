#!/usr/bin/python3
"""
<<<<<<< HEAD
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
A simple flask server running on 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states', strict_slashes=False)
def display_states():
    """Prints html document with a list of states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>')
def get_state(id):
    """Prints html document with a state and it's cities"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def remove_current_session(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> d364182adf6b6aebc07fd37d00692d0bd7608f44
