#!/usr/bin/python3
"""First Module"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """rendered at path (/) """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_world_hbnb():
    """rendered at path (/hbnb) """
    return "HBNB"


if __name__ == "__main__":
    """main method"""
    app.run(host="0.0.0.0", port=5000)
