from flask import Flask, flash, redirect, render_template, request, session, url_for, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from urllib.parse import quote_plus, urlencode
from os import environ as env


# Configure Flask application
app = Flask(__name__)

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if 'file' not in request.files:
        return 'No file part in the request', 400
    file = request.files['file']
    with open("temp.txt", "r") as f:
        text=f.read()
    return jsonify({"text": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=env.get("PORT", 5000)) 