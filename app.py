from distutils.log import debug
from email.policy import default
from flask import Flask, jsonify

app = Flask(__name__)


# Especifica a rota para qual quer se escrever código.
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/home', methods=['POST', 'GET'], defaults={'name': 'Default'})
@app.route('/home/<string:name>', methods=['GET', 'POST'])
def home(name):
    return '<h1>Hello {}, você está na homepage</h1>'.format(name)


@app.route('/json')
def json():
    return jsonify({'key':'value', 'listkey2': [1, 2, 3]})



if __name__ == '__main__':
    app.run(debug=True)