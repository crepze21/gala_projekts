from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect("static/data.db")


@app.route("/")
def index():
    return render_template("index.html")

#palaiž mājaslapu
if __name__ == "__main__":
    app.run(debug=True)