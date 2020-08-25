import sqlite3
from flask import Flask, jsonify, g

app = Flask(__name__)

DATABASE = 'database.db'


def get_db():
    """ 
    Function make use of Flask Global object to share db connection
    Function return the db connect
     """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.route('/pokemon')
def pokemon():
    c = get_db().cursor()
    results = c.execute("SELECT * FROM pokemon")
    pokemon_info = []
    for row in results:
        pokemon_info.append(dict(row))
    return jsonify(pokemon_info)


@app.route("pokemon/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_poke_by_id(id):
    c = get_db().cursor()
    results = c.execute("SELECT * FROM pokemon WHERE pokeId =" + str(id))
    pokemon_info = []
    for row in results:
        pokemon_info.append(dict(row))
    return jsonify(pokemon_info)


if __name__ == '__main__':
    app.run(debug=True)
