from flask import Flask, render_template, jsonify
import os 
from conn import coll

PORT = int(os.environ.get('PORT', 8000))
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'backend running'})

@app.route('/api/get')
def data():
    names = coll.find()
    result = []
    for name in names:
        result.append(name['value'])  # make sure it's 'value' not 'values'

    return jsonify({"data": result})

@app.route('/api/add/<name>')
def getval(name):
    coll.insert_one({'value': name})
    return jsonify({'message': 'added'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
