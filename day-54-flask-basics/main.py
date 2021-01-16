from flask import Flask

app = Flask(__name__)


@app.route("/")
def hi():
    return "hi there pal"


@app.route("/xyz")
def xyz():
    return "xyz"


@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
