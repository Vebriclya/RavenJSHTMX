from flask import Flask, render_template, request
from db import sample_db

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/posts")
def posts():
    posts = sample_db.get_posts()
    return render_template("posts.html", posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    post = sample_db.get_post(post_id)
    return render_template("_partials/postcard.html", post=post)


@app.route("/posts/edit/<int:post_id>", methods=["GET", "PUT"])
def edit_post(post_id):
    if request.method == "PUT":
        title = request.form.get("title")
        content = request.form.get("content")
        sample_db.update_post(post_id, title=title, content=content)
        return show_post(post_id)
    # Default GET behaviour
    post = sample_db.get_post(post_id)
    return render_template("_partials/edit.html", post=post)
