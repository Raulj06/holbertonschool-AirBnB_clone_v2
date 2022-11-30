#!/usr/bin/python3


"""start the Flask Web application by"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def holberton_school():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)