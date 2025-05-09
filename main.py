from flask import Flask, render_template, request, session
from datubaze import *

app = Flask(__name__)



@app.route('/')
def index():
    past_tournaments = ['IEM MELBOURNE 2025 CHAMPIONS', 'TEAM VITALITY', 'ZywOo', 'Ropz', 'apEX', 'flameZ', 'mezii']
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
    turnira_nosaukums = "ESL Pro League Season - 21"
    trn_nosaukums = turnira_nosaukums
    global turnira_sais
    turnira_sais = "ESL"
    pieteikta_kmd = kommanda(request.form.get("kmd_nosaukums"),
                             request.form.get("kpt_steam_vards"),request.form.get('kpt_vards'),request.form.get('kpt_uzvards'),
                             request.form.get("kpt_steam_vards"),request.form.get('kpt_vards'),request.form.get('kpt_uzvards'),
                             request.form.get("kpt_steam_vards"),request.form.get('kpt_vards'),request.form.get('kpt_uzvards'),
                             request.form.get("kpt_steam_vards"),request.form.get('kpt_vards'),request.form.get('kpt_uzvards'),
                             request.form.get("kpt_steam_vards"),request.form.get('kpt_vards'),request.form.get('kpt_uzvards'),
                             turnira_sais
                             )
    turnirs = tabula(f"static/{turnira_sais}.db",turnira_sais)
    turnirs.ierakstit_kommandu(pieteikta_kmd.get_all())

    return render_template('pieteikts.html', kmd_nosaukums=pieteikta_kmd.__str__(), trn_nosaukums=trn_nosaukums )


if __name__ == "__main__":
    app.run(debug=True)