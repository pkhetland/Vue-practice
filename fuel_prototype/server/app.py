import sqlite3
from flask import Flask, jsonify, g
from flask_cors import CORS

DATABASE = './cards.db'

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

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Send full card JSON
@app.route('/cards', methods=['GET'])
def all_cards():
    get_db().row_factory = sqlite3.Row
    cur = get_db().cursor()
    result = cur.execute("SELECT * FROM cards")
    return jsonify([dict(zip([key[0] for key in cur.description], row)) for row in result if row['text'] != ""])

# Send categorical card JSONs
@app.route('/relationship', methods=['GET'])
def relationship_category():
    get_db().row_factory = sqlite3.Row
    cur = get_db().cursor()
    result = cur.execute("SELECT * FROM cards WHERE category='relationship'")
    return jsonify([dict(zip([key[0] for key in cur.description], row)) for row in result])


if __name__ == '__main__':
    app.run()