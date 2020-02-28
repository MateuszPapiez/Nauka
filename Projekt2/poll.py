from flask import Flask, render_template, request

# Globala definicja zmiennych

app = Flask(__name__)

poll_data = {
    'question': 'Pies czy Kot?',
    'fields': ['Pies', 'Kot']
}

@app.route("/")
def strona_glowna():
    return render_template("strona_glowna.html",dane=poll_data)

@app.route('/poll')

def poll():
    vote=request.args.get('field')
    with open("wyniki.txt", "a") as wyniki:
        wyniki.write("{}\n".format(vote))
    with open("wyniki.txt","r") as wyniki:
        wynik=wyniki.read()
    wyniki_zwierzakow={}
    for zwierze in poll_data["fields"]:
        wyniki_zwierzakow[zwierze]=wynik.count(zwierze)
    #psy=(wynik.count('Pies'))
    #koty=(wynik.count('Kot'))

    #ankieta=("Pies {}, Kot {}".format(psy,koty))


    return render_template('wyniki.html',vote=wyniki_zwierzakow,dane=poll_data)



app.run(debug=True)
#projekt 4
