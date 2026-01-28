import bcrypt
from flask import Flask, redirect, render_template, request

# create Flask object
app = Flask(__name__)


# if access the route (/)
@app.route("/")
def index():
    return render_template("loginPage.html")


# if access the route (/checkLogin)
@app.route("/checkLogin", methods=["GET", "POST"])
def verifyLogin():
    correctLog = "dvtzoe"  # your login
    correctPassHash = (
        "$2a$04$pTb2y3146QquRJBEl5pbfuizrglsNGhZrTPwVe0foIVM0OEQtcb1K"  # your password
    )
    bodyContent = "<center>You are not permited to this site !</center>"
    if request.method == "POST":
        getLog = request.form["login"]
        getPass = request.form["passwd"]

        # Your implementation if your login and passwod are correct
        if getLog == correctLog and bcrypt.checkpw(
            getPass.encode("utf-8"), correctPassHash.encode("utf-8")
        ):
            bodyContent = "<center>Welcome to the site !</center>"
        return bodyContent

    elif request.method == "GET":
        getLog = request.args.get("login")
        getPass = request.args.get("passwd")

        if not getPass:
            return bodyContent

        # Your implementation if your login and passwod are correct
        if getLog == correctLog and bcrypt.checkpw(
            getPass.encode("utf-8"), correctPassHash.encode("utf-8")
        ):
            bodyContent = "<center>Welcome to the site !</center>"
        return bodyContent

    else:
        return redirect("https://www.google.com/")


app.run(host="0.0.0.0", port=5000)
