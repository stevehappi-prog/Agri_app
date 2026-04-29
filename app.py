from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

def get_db():
    return sqlite3.connect('database.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        nom = request.form.get('nom_culture')
        surface = request.form.get('surface')
        quantite = request.form.get('quantite')
        pluie = request.form.get('pluie')
        date = request.form.get('date')

        conn = get_db()
        c = conn.cursor()
        
        c.execute("""
              INSERT INTO cultures (nom_culture, surface, quantite, pluie, date) VALUES (?, ?, ?, ?, ?)",
              (nom, surface, quantite, pluie, date)
              VALUES (?,?,?,?)
              """, (nom, surface, quantite, pluie, date))
        
        conn.commit()
        conn.close()

        return redirect('/dashboard')

    except Exception as e:
        return str(e)

@app.route('/dashboard')
def dashboard():
    conn = get_db()
    c = conn.cursor()

    # total enregistrements
    c.execute("SELECT COUNT(*) FROM cultures")
    total = c.fetchone()[0]

    # quantité totale
    c.execute("SELECT SUM(quantite) FROM cultures")
    total_quantite = c.fetchone()[0] or 0

    # surface totale
    c.execute("SELECT SUM(surface) FROM cultures")
    total_surface = c.fetchone()[0] or 0

    # rendement moyen
    rendement = 0
    if total_surface != 0:
        rendement = total_quantite / total_surface

    conn.close()

    return render_template("dashboard.html",
                           total=total,
                           total_quantite=total_quantite,
                           rendement=rendement)

    import os
if __name__== "__main__":    
        port = int(os.environ.get("PORT",5000))
        app.run(host="0.0.0.0", port=port, debug=True)

