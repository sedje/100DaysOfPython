import requests
from mailer import Mailer
from flask import Flask, render_template, request


app = Flask(__name__)

all_posts = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
mailer = Mailer()


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


@app.route("/send", methods=['POST'])
def send_email():
    form_data = request.form

    email_content = f"Name: {form_data['name']}\n" \
                    f"E-mail: {form_data['email']}\n" \
                    f"Phone: {form_data['phone']}\n\n" \
                    f"{form_data['message']}"

    mailer.send_mail(message=email_content)

    return render_template("sent.html")


if __name__ == "__main__":
    app.run()
