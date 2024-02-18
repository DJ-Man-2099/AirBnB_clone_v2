#!/usr/bin/python3
"""First Module"""

import os
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def hello_world_states_list():
    """rendered at path (/) """
    states = list(sorted(storage.all("State").values(), key=lambda x: x.name))
    return render_template('7-states_list.html', states=states)


@app.route("/cities_by_states", strict_slashes=False)
def hello_world_cities_by_states():
    """rendered at path (/) """
    states_pre_map = storage.all("State").values()
    sorted_states_pre_map = sorted(states_pre_map, key=lambda x: x.name)
    states = list(
        map(add_and_sort_cities, sorted_states_pre_map))
    return render_template('8-cities_by_states.html', states=states)


def add_and_sort_cities(state):
    """adds and sorts cities"""
    state.sorted_cities = sorted(state.cities, key=lambda x: x.name)
    return state


@app.teardown_appcontext
def on_teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    """main method"""
    app.run(host="0.0.0.0", port=5000)
