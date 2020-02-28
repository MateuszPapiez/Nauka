from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")

def wczytaj_plik():
    with open("olx.csv", "r") as f:
        dane = f.read()
        dane=dane.split('\n')
        dane2=[]
        for linia in dane:
            splited=linia.split(',')
            dane2.append(splited)

    return render_template('strona_glowna.html',dane=dane2)

app.run(debug=True)