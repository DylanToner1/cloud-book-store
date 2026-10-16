from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello to you too"


@app.route("/books", methods=["GET"])
def books():
    return render_template("books.html")


@app.route("/authors", methods=["GET"])
def authors():
    return [
        {"name": "Julia Donaldson", "dob": "1948-09-16"},
        {"name": "Andrea Beaty", "dob": "1961-10-08"},
        {"name": "Kelly Barnhill", "dob": "1973-01-01"},
        {"name": "Zetta Elliott", "dob": "1979-11-11"},
    ]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
