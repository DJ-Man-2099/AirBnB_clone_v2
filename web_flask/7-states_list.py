#!/usr/bin/python3
"""First Module"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def hello_world_states_list():
    """rendered at path (/) """
    try:
        states = storage.all("State").values()
    except Exception as e:
        states = []
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def on_teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    """main method"""
    app.run(host="0.0.0.0", port=5000)
