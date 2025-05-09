from flask import Flask, render_template, request, session
from datubaze import *

app = Flask(__name__)



@app.route('/')
def index():
    conn = sqlite3.connect("static/ESL.db")
    pirma_vieta = conn.execute("SELECT pirma_vieta FROM turnirs WHERE id = 1").fetchone()
    otra_vieta = conn.execute("SELECT otra_vieta FROM turnirs WHERE id = 1").fetchone()
    tresa_vieta = conn.execute("SELECT tresa_vieta FROM turnirs WHERE id = 1").fetchone()
    past_tournaments = ['IEM MELBOURNE 2025 CHAMPIONS', f"1. {pirma_vieta[0]}", f"2. {otra_vieta[0]}", f"3. {tresa_vieta[0]}"]
    return render_template('index.html', past_tournaments=past_tournaments)

@app.route('/rules')
def rules():
    rules = [
        
    ]
    return render_template('rules.html', rules=rules)

@app.route('/tournaments')
def tournaments():

    return render_template('tournaments.html')

@app.route('/registracija/ESL')
def registracija_ESL():
    nosaukums = "ESL Pro League Season - 21"
    global turnira_sais
    global turnira_nosaukums
    turnira_nosaukums = nosaukums
    turnira_sais = "ESL"
    return render_template('registracija.html', nosaukums_trn=nosaukums)
    

@app.route('/registracija/IEM', methods=['GET','POST'])
def registracija_IEM():
    nosaukums = "IEM Dallas"
    global turnira_sais
    global turnira_nosaukums
    turnira_nosaukums = nosaukums
    turnira_sais = "IEM"
    return render_template('registracija.html', nosaukums_trn=nosaukums)

@app.route('/registracija/BLASTtv', methods=['GET','POST'])
def registracija_BLASTtv():
    nosaukums = "BLAST.tv Austin Major 2025"
    global turnira_sais
    global turnira_nosaukums
    turnira_nosaukums = nosaukums
    turnira_sais = "BLASTtv"
    return render_template('registracija.html', nosaukums_trn=nosaukums)

@app.route('/pieteikts', methods=['GET','POST'])
def pieteikts():
    
    global turnira_nosaukums

    global turnira_sais

    pieteikta_kmd = kommanda(request.form.get("kmd_nosaukums"),
                             request.form.get("kpt_steam_vards"),request.form.get('kpt_vards'),request.form.get('kpt_uzvards'),
                             request.form.get("spl_1_steam_vards"),request.form.get('spl_1_vards'),request.form.get('spl_1_uzvards'),
                             request.form.get("spl_2_steam_vards"),request.form.get('spl_2_vards'),request.form.get('spl_2_uzvards'),
                             request.form.get("spl_3_steam_vards"),request.form.get('spl_3_vards'),request.form.get('spl_3_uzvards'),
                             request.form.get("spl_4_steam_vards"),request.form.get('spl_4_vards'),request.form.get('spl_4_uzvards'),
                             turnira_nosaukums
                             )
    
    turnirs = tabula(f"static/{turnira_sais}.db",turnira_nosaukums)
    turnirs.ierakstit_kommandu(pieteikta_kmd.get_all())

    return render_template('pieteikts.html', kmd_nosaukums=pieteikta_kmd.__str__(), trn_nosaukums=turnira_nosaukums )


if __name__ == "__main__":
    app.run(debug=True)