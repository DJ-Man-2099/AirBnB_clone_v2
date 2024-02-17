#!/usr/bin/python3
"""First Module"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def hello_world():
    """rendered at path (/) """
    states = list(sorted(storage.all("State").values(), key=lambda x: x.name))
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def on_teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    """main method"""
    app.run(host="0.0.0.0", port=5000)
