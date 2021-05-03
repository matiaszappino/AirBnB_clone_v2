#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask
from models import storage
from flask import render_template


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def stateslist(state):
    """Displays a HTML page"""
    states_list = storage.all("State")
    return render_template("7-states_list.html", states_list)

@app.teardown_appcontext
def teardown_close():
    """Calls close method"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
