from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

all_posts = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()


@app.route("/")
def main():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:post_id>")
def post(post_id):
    return render_template("post.html", posts=all_posts[post_id])


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
