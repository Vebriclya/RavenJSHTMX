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


@app.route("/posts/edit/<int:post_id>")
def edit_post(post_id):
    post = sample_db.get_post(post_id)
    return render_template("_partials/edit.html", post=post)
