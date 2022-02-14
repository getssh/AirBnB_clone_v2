#!/usr/bin/python3

'''using parametrs with falsk'''


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greet():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def sub_greet():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def disp_python(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
