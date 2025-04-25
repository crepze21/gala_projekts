from flask import Flask, render_template, request
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
             kapteina_steam_id TEXT,
             PRIMARY KEY("id")
             )""")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registration", methods=["GET","POST"])
def registration():
    nosaukums = request.form.get("nosaukums")
    name_kaptain = request.form.get("name_kaptain")
    steam_id_kaptain = request.form.get("steam_id_kaptain")
    name_speletajs_1 = request.form.get("name_speletajs_1")
    name_speletajs_2 = request.form.get("name_speletajs_2")
    name_speletajs_3 = request.form.get("name_speletajs_3")
    name_speletajs_4 = request.form.get("name_speletajs_4")
    steam_id_1 = request.form.get("steam_id_1")
    steam_id_2 = request.form.get("steam_id_2")
    steam_id_3 = request.form.get("steam_id_3")
    steam_id_4 = request.form.get("steam_id_4")
    kommanda = [nosaukums, name_kaptain, steam_id_kaptain, name_speletajs_1, name_speletajs_2, name_speletajs_3, name_speletajs_4, steam_id_1,steam_id_2,steam_id_3,steam_id_4]
    
    for i in kommanda:
        if kommanda == "" or None:
            kluda = True
            break
        else:
            kluda = False

    return render_template("registration.html", kluda=kluda)

#palaiž mājaslapu
if __name__ == "__main__":
    app.run(debug=True, port=5001)