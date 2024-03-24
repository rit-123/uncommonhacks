from flask import Flask, flash, redirect, render_template, request, session, url_for, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from urllib.parse import quote_plus, urlencode
from os import environ as env


# Configure Flask application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )

# This route is the called after authentication
@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )

@app.route("/")
def home():
    #return render_template("index.html") - this isnot referencing the index.html file correctly in the templates folder, fix it
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=env.get("PORT", 3000)) 