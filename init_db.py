import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS cultures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_culture TEXT,
    surface REAL,
    quantite REAL,
    pluie REAL,
    date TEXT
)
""")

conn.commit()
conn.close()

print("Base de donnees créée")

