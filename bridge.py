from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
# Allows your browser to talk to this cloud VM
CORS(app)

@app.route('/get_session', methods=['POST'])
def proxy_tradier():
    api_key = request.headers.get('Authorization')
    # This Python script handles the Tradier request to bypass CORS
    response = requests.post(
        'https://api.tradier.com/v1/markets/events/session',
        data={},
        headers={'Authorization': api_key, 'Accept': 'application/json'}
    )
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    # Cloud environments require listening on 0.0.0.0
    app.run(host='0.0.0.0', port=5000)