from flask import Flask, send_from_directory, jsonify
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CLIENT_DIR = os.path.join(BASE_DIR, "client", "dist")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__)
app.secret_key = "Developer Key"


@app.route('/')
def index():
    return send_from_directory(CLIENT_DIR, "index.html")


@app.route('/<path:filename>')
def client_app(filename):
    return send_from_directory(CLIENT_DIR, filename)


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(STATIC_DIR, filename)


@app.route('/api/items')
def data():
    reply = {
      "results": [
        "Item 1",
        "Item 2",
      ]
    }

    return jsonify(result=reply)