from flask_sqlalchemy import SQLAlchemy


class Database:

    def __init__(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://books-collection.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db = SQLAlchemy(app)

        class Book(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(80))
            author = db.Column(db.String(80))
            rating = db.Column(db.Integer)

            def __repr__(self):
                return '<Book %r>' % self.name

    def add_book(self, book):
        new_book = Book(
            id=book['id'],
            title=book["name"],
            author=book["author"],
            rating=book['rating'])
        self.db.session.add(new_book)
        self.db.session.commit()