from flask import Flask, redirect

app = Flask(__name__)


@app.route("/kosen")
def kosen():
    return redirect("https://www.kosen-k.go.jp/")


@app.route("/github")
def github():
    return redirect("https://github.com/dvtzoe")


@app.route("/rickroll")
def rickroll():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


if __name__ == "__main__":
    app.run()
