from flask import Flask, request, redirect
from flask.templating import render_template
import requests
from flask.helpers import make_response, url_for

app = Flask(__name__)


@app.route('/')
def index():
    caught = requests.get('http://127.0.0.1:5000/caught')
    debug = caught.json()
    return render_template("index.html", caught=debug)


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
    isLoggedIn = request.cookies.get('user')
    if isLoggedIn:
        return render_template("add.html")
    return redirect(url_for('login', error="Please login to add pokemon"))


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
    if request.cookies.get('user'):
        return render_template("login.html", error=request.args.get('error'), user=request.cookies.get('user'), isLoggedIn=True)
    return render_template("login.html", error=request.args.get('error'))


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
    resp = make_response(render_template(
        "login.html", isLoggedIn=True, user=user['email']))
    resp.set_cookie('user', user['email'])
    return resp


if __name__ == '__main__':
    app.run(debug=True, port=8000)
