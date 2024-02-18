#!/usr/bin/python3
"""First Module"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """rendered at path (/) """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_world_hbnb():
    """rendered at path (/hbnb) """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_world_c_text(text):
    """rendered at path (/c/<text>) """
    return f"C {text.replace('_',' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def hello_world_number_n(n):
    """rendered at path (/number/<n>) """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def hello_world_number_template_n(n):
    """rendered at path (/number/<n>) """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def hello_world_number_odd_or_even_n(n):
    """rendered at path (/number/<n>) """
    string = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, string=string)


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_world_python_text(text):
    """rendered at path (/python/<text>) """
    return f"Python {text.replace('_',' ')}"


@app.route("/states_list", strict_slashes=False)
def hello_world_states_list():
    """rendered at path (/) """
    states = list(sorted(lambda x: x.name, storage.all("State").values()))
    return render_template('7-states_list.html', states=states)


@app.route("/states_list", strict_slashes=False)
def hello_world_states_list():
    """rendered at path (/) """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def on_teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    """main method"""
    app.run(host="0.0.0.0", port=5000)
