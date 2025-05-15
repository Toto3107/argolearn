from flask import Flask, render_template
import os
import requests

PORT = os.environ.get('PORT', 5000)
app = Flask(__name__)
BACKEND_URL = os.environ.get('BACKEND_URL','localhost:8000')
@app.route('/')
def index():
    env = dict(os.environ)
    response = requests.get(f'{BACKEND_URL}/api/get')
    data = response.json()
    
    return render_template('index.html', env = env, data = data['data'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
