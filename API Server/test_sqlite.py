import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)



@app.route('/')
def pokemon():
    conn = sqlite3.connect('pokemon.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    results = c.execute("SELECT * FROM pokemon")
    pokemon_info = []
    for row in results:
        pokemon_info.append(dict(row))
    return jsonify(pokemon_info)

@app.route("/<int:id>")
def get_poke_by_id(id):
    conn = sqlite3.connect('pokemon.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    results = c.execute("SELECT * FROM pokemon WHERE pokedexID =" + str(id))
    pokemon_info = []
    for row in results:
        pokemon_info.append(dict(row))
    return jsonify(pokemon_info)


if __name__ == '__main__':
    app.run(debug=True)
