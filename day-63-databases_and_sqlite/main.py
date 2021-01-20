from flask import Flask, render_template, request, redirect, url_for
# from database import Database
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


all_books = []
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    author = db.Column(db.String(80))
    rating = db.Column(db.Integer)

    def __repr__(self):
        return '<Book %r>' % self.name

@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        form = request.form
        all_books.append({'name': form['name'], 'author': form['author'], 'rating': form['rating']})
        return redirect(url_for('home'))

    return render_template("add.html")


if __name__ == "__main__":
    app.run()

