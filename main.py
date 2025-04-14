from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect("static/data.db")

conn.execute("""CREATE TABLE IF NOT EXISTS speletaji(
             id INTEGER,
             vards TEXT,
             uzvards TEXT,
             steam_id TEXT,
             komandas_id INTEGER,
             PRIMARY KEY("id"),
             FOREIGN KEY (komandas_id) REFERENCES kommandas (id)
             ) """)

conn.execute("""CREATE TABLE IF NOT EXISTS kommandas(
             id INTEGER,
             nosaukums TEXT,
             kapteina_steam_id,
             PRIMARY KEY("id")
             )""")

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/regi")
def regi():
    return render_template("regi.html")

#palaiž mājaslapu
if __name__ == "__main__":
    app.run(debug=True)