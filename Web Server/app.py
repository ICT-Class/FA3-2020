from flask import Flask, request
from flask.templating import render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    caught = requests.get('http://127.0.0.1:5000/caught')
    return render_template("index.html", caught=caught.json())


@app.route('/firstpokemon')
def firstpokemon():
    response = requests.get('http://127.0.0.1:5000/22')
    # print(response.json())
    return render_template("poke_info.html", pokemon=response.json()[0])


if __name__ == '__main__':
    app.run(debug=True, port=8000)
