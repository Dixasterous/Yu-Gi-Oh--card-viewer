from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)


API_URL = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
bob = 'bob bob bob'
print(bob.replace(' ', '%20'))

def fetch_cards():
    response = requests.get(API_URL)
    return response.json()['data']

def get_card_info(cards_data,query,card_type):
    matched_cards = []
    
    for card in cards_data:
        if card_type in card['type']:
            if query in card['name'].lower():  # if no query, it will just return all monsters.if query, it will only return and the monsters into the list that match the query
                matched_cards.append(card)
    return matched_cards


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/all')
def all():
    query = request.args.get('query', '').lower()  # if theres query, get it, else just return empty string
    cards_data = fetch_cards()
    
    monsters = (get_card_info(cards_data,query,"Monster"))
    
    spells = (get_card_info(cards_data,query,"Spell"))
    
    traps = (get_card_info(cards_data,query,"Trap"))
    
    return render_template('all.html',monsters=monsters,spells=spells,traps=traps,query=query)


@app.route('/Monsters')
def monsters():
    query = request.args.get('query', '').lower()  # if theres query, get it, else just return empty string
    cards_data = fetch_cards()
    
    monsters = (get_card_info(cards_data,query,"Monster"))

    return render_template('monsters.html', monsters=monsters,query=query)


@app.route("/Spells")
def spells():
    query = request.args.get('query', '').lower()  # if theres query, get it, else just return empty string
    cards_data = fetch_cards()
    
    spells = (get_card_info(cards_data,query,"Spell"))

    return render_template('spells.html', spells=spells,query=query)

@app.route("/Traps")
def traps():
    cards_data = fetch_cards()
    query = request.args.get('query', '').lower()  # if theres query, get it, else just return empty string
    
    traps = (get_card_info(cards_data,query,"Trap"))
            
    return render_template('traps.html', traps=traps,query=query)



if __name__ == '__main__':
    app.run(debug=True)
