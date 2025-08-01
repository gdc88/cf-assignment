from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def headers():
    headers = dict(request.headers)
    return json.dumps(headers, indent=2), 200, {'Content-Type': 'application/json'}
