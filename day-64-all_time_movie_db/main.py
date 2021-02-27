from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    year = db.Column(db.Integer)
    description = db.Column(db.String(80))
    rating = db.Column(db.Integer)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(80))
    img_url = db.Column(db.String(80))

    def __repr__(self):
        return '<Movie %r>' % self.title


class EditForm(FlaskForm):
    rating = StringField(label='Your rating out of 10, e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


# try/catch to see if the DB exists, if not, create and fill with data.
try:
    f = open("movie-collection.db")
except IOError:
    db.create_all()
    new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an "
                    "extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with "
                    "the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    )
    db.session.add(new_movie)
    db.session.commit()


@app.route("/")
def home():
    # movies = db.session.query(Movie).order_by(Movie.rating.desc()).limit(10).all()
    all_movies = db.session.query(Movie).order_by(Movie.rating.desc()).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = 1 + i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit/<int:movie_id>", methods=['GET', 'POST'])
def edit(movie_id):
    form = EditForm()
    if form.validate_on_submit():
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = form.rating.data
        movie_to_update.reviewtop = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", edit_form=form)


@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    db.session.delete(Movie.query.get(movie_id))
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
@app.route("/add/<int:movie_id>", methods=['GET', 'POST'])
def add(movie_id=None):
    form = AddForm()
    if form.validate_on_submit():
        url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": os.getenv("API_KEY"),
            "language": "en-US",
            "query": form.title.data,
            "include_adult": "false"
        }
        movie = requests.get(url, params=params).json()
        return render_template("select.html", movies=movie['results'])

    if movie_id:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        params = {
            "api_key": os.getenv("API_KEY")
        }
        movie = requests.get(url, params=params).json()
        add_movie = Movie(
            title=movie['original_title'],
            year=movie['release_date'].split('-')[0],
            description=movie['overview'],
            img_url=f"https://image.tmdb.org/t/p/w300/{movie['poster_path']}"
        )
        db.session.add(add_movie)
        db.session.commit()
        return redirect(url_for('edit', movie_id=add_movie.id))

    return render_template("add.html", add_form=form)


if __name__ == '__main__':
    app.run()
