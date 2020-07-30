import sqlite3
conn = sqlite3.connect('pokemon.db')
c = conn.cursor()
results = c.execute("SELECT * FROM pokemon")
for row in results:
    print(row)