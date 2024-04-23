from flask import Flask, render_template
from db import sample_db

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/posts")
def posts():
    posts = sample_db.get_posts()
    return render_template("posts.html", posts=posts)
