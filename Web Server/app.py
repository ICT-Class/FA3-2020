from flask import Flask, request
from flask.templating import render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    caught = requests.get('http://127.0.0.1:5000/caught')
    return render_template("index.html", caught=caught.json())


@app.route('/pokemon')
def firstpokemon():
    response = requests.get('http://127.0.0.1:5000/pokemon')
    # print(response.json())
    return render_template("pokemon.html", pokemons=response.json())


@app.route('/add')
def add():
    return render_template("add.html")


@app.route('/add', methods=['POST'])
def response():
    newPoke = {
        "name": request.form.get("name"),
        "hp": request.form.get("hp"),
        "attack": request.form.get("attack"),
        "defense": request.form.get("defense"),
        "speed": request.form.get("speed"),
        "image": request.form.get("image"),
    }
    requests.post('http://127.0.0.1:5000/pokemon/add', json=newPoke)
    return render_template("add.html", name=newPoke['name'], hp=newPoke["hp"], attack=newPoke["attack"], defense=newPoke["defense"], speed=newPoke['speed'], image=newPoke['image'])


if __name__ == '__main__':
    app.run(debug=True, port=8000)
