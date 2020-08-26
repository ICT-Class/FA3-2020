from flask import Flask, request
from flask.templating import render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    caught = requests.get('http://127.0.0.1:5000/caught')
    return render_template("index.html", caught=caught.json())


@app.route('/search/pokemon')
def search_pokemon():
    searchtext = request.args.get('searchtext')
    pokemons = requests.get(
        'http://127.0.0.1:5000/search/pokemon', params={'searchtext': searchtext})
    return render_template("search.html", pokemons=pokemons.json(), searchtext=searchtext)


@app.route('/search/user')
def search_user():
    searchtext = request.args.get('searchtext')
    users = requests.get(
        'http://127.0.0.1:5000/search/user', params={'searchtext': searchtext})
    return render_template("search.html", users=users.json(), searchtext=searchtext)


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


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/user/create', methods=['POST'])
def create_user():
    user = {
        "email": request.form.get("email"),
        "password": request.form.get("password"),
    }
    requests.post("http://127.0.0.1:5000/user/create", json=user)
    return render_template("login.html", email=user['email'], password=user['password'])


@app.route('/user/login', methods=['POST'])
def login_user():
    user = {
        "email": request.form.get("email"),
        "password": request.form.get("password"),
    }
    response = requests.post("http://127.0.0.1:5000/user/login", json=user)
    isLoggedIn = response.text.rstrip()
    if isLoggedIn == 'false':
        return render_template("login.html", isLoggedIn=False, error="Incorrect login or password")
    return render_template("login.html", isLoggedIn=True, user=user['email'])


if __name__ == '__main__':
    app.run(debug=True, port=8000)
