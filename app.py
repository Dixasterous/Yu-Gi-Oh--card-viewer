from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

# add search bar feature later

API_URL = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'

def fetch_cards():
    response = requests.get(API_URL)
    return response.json()['data']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Monsters')
def monsters():
    cards_data = fetch_cards()
    monsters = []

    for card in cards_data:
        if 'Monster' in card['type']:
            monsters.append(card)
    
    return render_template('monsters.html', monsters=monsters)

@app.route("/Spells")
def spells():
    cards_data = fetch_cards()
    spells = []

    for card in cards_data:
        if 'Spell' in card['type']:
            spells.append(card)
            
    return render_template('spells.html', spells=spells)

@app.route("/Traps")
def traps():
    cards_data = fetch_cards()
    traps = []

    for card in cards_data:
        if 'Trap' in card['type']:
            traps.append(card)
            
    return render_template('traps.html', traps=traps)

if __name__ == '__main__':
    app.run(debug=True)
