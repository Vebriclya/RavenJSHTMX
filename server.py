from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/posts")
def posts():
    return render_template("posts.html")
