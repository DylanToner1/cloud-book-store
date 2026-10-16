from flask import Flask, redirect, render_template, request

from lib.book_repo import BookRepository
from lib.db_conn import DatabaseConnection
from lib.models.book import Book

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello to you too"


@app.route("/books", methods=["GET"])
def books():
    conn = DatabaseConnection()
    conn.connect()

    book_repo = BookRepository(conn)

    books = book_repo.all()

    return render_template("books.html", books=books)


@app.route("/books", methods=["POST"])
def create_book():
    book_details = request.form

    title = book_details.get("title")
    author = book_details.get("author")

    if not title or not author:
        return "values can't be blank", 400

    conn = DatabaseConnection()
    conn.connect()

    book_repo = BookRepository(conn)

    book_repo.create(Book(id=0, title=title, author=author))
    return redirect("/books")


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
