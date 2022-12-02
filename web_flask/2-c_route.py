#!/usr/bin/python3
""" Script that starts a Flask Web Application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def startup():
    """ Displays message on / route """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays message on /hbnb route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Displays message on /c route """
    text = text.replace('_', " ")
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
