#!/usr/bin/python3
"""First Module"""

import os
from models import storage
from flask import Flask, render_template

app = Flask(__name__, static_folder="static", static_url_path="/")


@app.route("/hbnb", strict_slashes=False)
def hello_world_hbnb():
    """rendered at path (/) """
    states = list(sorted(storage.all("State").values(), key=lambda x: x.name))
    amenities = list(
        sorted(storage.all("Amenity").values(), key=lambda x: x.name))
    places = list(
        sorted(storage.all("Place").values(), key=lambda x: x.name))
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def on_teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    """main method"""
    app.run(host="0.0.0.0", port=5000)
