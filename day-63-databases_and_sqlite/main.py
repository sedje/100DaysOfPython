from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    author = db.Column(db.String(80))
    rating = db.Column(db.Integer)

    def __repr__(self):
        return '<Book %r>' % self.name

# try/catch to see if the DB exists, if not, create and fill with data.
try:
    f = open("books-collection.db")
except IOError:
    db.create_all()
    new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=6)
    db.session.add(new_book)
    db.session.commit()
    new_book = Book(title="Lord of the Rings", author="J. R. R. Tolkien", rating=7)
    db.session.add(new_book)
    db.session.commit()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        form = request.form
        new_book = Book(title=form['name'], author=form['author'], rating=form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html")


@app.route("/edit/<int:book_id>", methods=['GET', 'POST'])
def edit(book_id):
    if request.method == "POST":
        form = request.form
        rating = form['rating']
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = rating
        db.session.commit()
        return redirect(url_for('home'))

    book = Book.query.filter_by(id=book_id).first_or_404()
    return render_template("edit.html", book=book)


@app.route("/delete/<int:book_id>")
def delete(book_id):
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()


