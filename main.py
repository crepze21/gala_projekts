from flask import Flask, render_template

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
    tournament = {
        "name": "ESL Pro League Season - 21 ",
        "dates": "30.04 - 12.05 ",
        "prize": "1 000 000 $"
    }
    return render_template('tournaments.html', tournament=tournament)

@app.route('/registracija')
def registracija():
    registracija = {

    }
    return render_template('registracija.html')
if __name__ == "__main__":
    app.run(debug=True)