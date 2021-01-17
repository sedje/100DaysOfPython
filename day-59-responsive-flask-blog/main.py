import requests
import smtplib
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv(".env")

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


@app.route("/send", methods=['POST'])
def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    email_content = f"Name: {name}\n" \
                    f"E-mail: {email}\n" \
                    f"Phone: {phone}\n\n" \
                    f"{message}"

    my_email = os.getenv('EMAIL')
    username = os.getenv('EMAIL_USERNAME')
    password = os.getenv('EMAIL_PASSWORD')
    subject = f"Subject:Website feedback\n\n"

    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=username, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"{subject}{email_content}")
    except smtplib.SMTPAuthenticationError:
        pass

    return render_template("sent.html")


if __name__ == "__main__":
    app.run()
