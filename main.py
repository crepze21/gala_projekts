from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    past_tournaments = ['CHAMPIONS2020', 'DS', 'DS', 'DS', 'DS', 'DS', 'DS', 'DS', 'DS', 'DS']
    return render_template('index.html', past_tournaments=past_tournaments)

@app.route('/rules')
def rules():
    rules = [
        'gfaojngfacfdsdsdfdfdssdfdafdfdfd',
        '2/.vbfbbfdbfbfdddddddddddddddddddd',
        '4.nsdasfdsdd4',
        'g/wgq', 'gd', 'b', 'r', 'hg', 'r'
    ]
    return render_template('rules.html', rules=rules)

@app.route('/tournaments')
def tournaments():
    tournament = {
        "name": "ESL Pro League Season - 21",
        "dates": "30.04 - 12.05",
        "prize": "1 000 000 $"
    }
    return render_template('tournaments.html', tournament=tournament)

if __name__ == "__main__":
    app.run(debug=True)