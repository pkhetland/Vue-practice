import sqlite3
from flask import Flask, jsonify, g, request
from flask_cors import CORS
from pymysql import NULL

DATABASE = 'cards.db'

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Send full card JSON
@app.route('/cards', methods=['GET', 'POST'])
def all_cards():

    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.json
        cur = get_db().cursor()
        if post_data.get('function') == 'add':
            cur.execute('INSERT INTO cards (title, category, text, rating) VALUES (?, ?, ?, ?)', 
            (post_data.get('title'), post_data.get('category'), post_data.get('text'), 0))
            get_db().commit()
            response_object['message'] = 'Card added!'

        elif post_data.get('function') == 'increase':

            rating = int(post_data.get('rating')) + 1
            cur.execute('UPDATE cards SET rating=? WHERE id=?', (rating, post_data.get('id')))
            get_db().commit()
            response_object['message'] = 'Rating updated!'
            response_object['new rating'] = rating

        elif post_data.get('function') == 'decrease':
            rating = int(post_data.get('rating')) - 1
            cur.execute('UPDATE cards SET rating=? WHERE id=?', (rating, post_data.get('id')))
            get_db().commit()
            response_object['message'] = 'Rating updated!'
            response_object['new rating'] = rating
        return jsonify(response_object, cur.lastrowid)

    if request.method == 'GET':
        get_db().row_factory = sqlite3.Row
        cur = get_db().cursor()
        result = cur.execute("SELECT * FROM cards")
        return jsonify([dict(zip([key[0] for key in cur.description], row)) for row in result if row['text'] != ""])

# Send categorical card JSONs
@app.route('/parkort', methods=['GET'])
def relationship_category():
    get_db().row_factory = sqlite3.Row
    cur = get_db().cursor()
    result = cur.execute("SELECT * FROM cards WHERE category='Parkort'")
    return jsonify([dict(zip([key[0] for key in cur.description], row)) for row in result])

@app.route('/vennekort', methods=['GET'])
def friendship_category():
    get_db().row_factory = sqlite3.Row
    cur = get_db().cursor()
    result = cur.execute("SELECT * FROM cards WHERE category='Vennekort'")
    return jsonify([dict(zip([key[0] for key in cur.description], row)) for row in result])

@app.route('/utfordring', methods=['GET'])
def challenge_category():
    get_db().row_factory = sqlite3.Row
    cur = get_db().cursor()
    result = cur.execute("SELECT * FROM cards WHERE category='Utfordring'")
    return jsonify([dict(zip([key[0] for key in cur.description], row)) for row in result])

if __name__ == '__main__':
    app.run()
