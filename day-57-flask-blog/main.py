from flask import Flask, render_template, request
import requests
import datetime
app = Flask(__name__)
year = datetime.datetime.now().year
all_posts = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()

@app.route("/")
@app.route("/<username>")
def home(username=None):
    if not username and not request.args.get('name'):
        return render_template("index.html", year=year)
    else:
        if username is None:
            username = request.args.get('name')
        gender = requests.get(f"https://api.genderize.io/?name={username}").json()
        age = requests.get(f"https://api.agify.io/?name={username}").json()
        user = { "name": username, "gender": gender['gender'], "age":age['age']}
        return render_template("index.html", user=user, year=year)


@app.route("/blog")
def blog():
    return render_template("blog.html", posts=all_posts, year=year)


@app.route("/blog/<int:post_id>")
def get_post(post_id):
    return render_template("post.html", posts=all_posts[post_id], year=year)


if __name__ == '__main__':
    app.run()
