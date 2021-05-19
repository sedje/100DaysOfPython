from random import choice

from flask import Flask, render_template, redirect, url_for, flash, abort, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6doNzWlSihBXox7C0sKR6b'
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    __tablename__ = "cafe"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route('/')
def home():
    cafes = db.session.query(Cafe).all()
    return render_template('index.html', cafes=cafes)


@app.route("/random")
def random():
    cafes = db.session.query(Cafe).all()
    random_cafe = choice(cafes)
    return render_template('cafe.html', cafe=random_cafe.to_dict())


@app.route("/all")
def get_all():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search/")
def search():

    cafes = Cafe.query.filter_by(location=request.args.get("location")).all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


@app.route("/add", methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route("/cafe/<int:cafe_id>")
def get_cafe(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    return render_template('cafe.html', cafe=cafe.to_dict())


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    update_cafe = db.session.query(Cafe).get(cafe_id)
    new_price = request.args.get("new_price")
    if update_cafe:
        update_cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>")
def report_closed(cafe_id):
    delete_cafe = db.session.query(Cafe).get(cafe_id)
    api_key = request.args.get("api-key")
    if api_key != "askdjn23d923nd2o3dnasdasd":
        return jsonify(response={"Access denied": "authorization required."}), 403

    if delete_cafe:
        db.session.delete(delete_cafe)
        db.session.commit()
        return jsonify(response={"Deleted": "Cafe succesfully deleted."}), 200
    return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
