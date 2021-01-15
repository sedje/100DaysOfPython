from flask import Flask, url_for
from flask import render_template
import random
app = Flask(__name__)

random_number = random.randint(0, 9)
@app.route("/")
def main():
    return render_template("number.html")


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return render_template("too_high.html")
    elif guess < random_number:
        return render_template("too_low.html")
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run()
