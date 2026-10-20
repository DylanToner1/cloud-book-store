import os
from decimal import Decimal

from flask import Flask, current_app, flash, redirect, render_template, request, session
from livereload import Server

from auth import login_required
from lib.book_repo import BookRepository
from lib.db_conn import DatabaseConnection
from lib.models.book import Book
from lib.models.user import User
from lib.user_repo import UserRepository


def get_db():
    # builds a database connection from the configured database url
    conn = DatabaseConnection(current_app.config["DB_URL"])
    conn.connect()
    return conn


def create_app(db_url=None):
    app = Flask(__name__)

    # the app uses whatever database we give it when starting
    app.config["DB_URL"] = db_url or os.getenv(
        "POSTGRES_URL", f"postgresql://localhost/{DatabaseConnection.DATABASE_NAME}"
    )

    app.secret_key = "some_really_secret_key"

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    @app.route("/books", methods=["GET"])
    def books():
        repo = BookRepository(get_db())

        books = repo.all()

        return render_template("books.html", books=books)

    @app.route("/books/new", methods=["GET"])
    @login_required
    def add_book_page():
        return render_template("addbook.html")

    @app.route("/books/new", methods=["POST"])
    @login_required
    def create_book():
        book_details = request.form

        title = book_details.get("title")
        author = book_details.get("author")
        synopsis = book_details.get("synopsis")
        rating = book_details.get("rating")
        notes = book_details.get("notes")

        if not title or not author:
            flash("Title or Author can't be blank!")
            return redirect("/books/new")

        repo = BookRepository(get_db())

        repo.create(
            Book(
                id=0,
                title=title,
                author=author,
                synopsis=synopsis,
                rating=Decimal(rating) if rating else None,
                notes=notes,
            )
        )
        return redirect("/books")

    @app.route("/authors", methods=["GET"])
    def authors():
        return [
            {"name": "Julia Donaldson", "dob": "1948-09-16"},
            {"name": "Andrea Beaty", "dob": "1961-10-08"},
            {"name": "Kelly Barnhill", "dob": "1973-01-01"},
            {"name": "Zetta Elliott", "dob": "1979-11-11"},
        ]

    @app.route("/signup", methods=["GET"])
    def signup():
        return render_template(
            "signup.html", username=session.pop("signup_username", "")
        )

    @app.route("/users", methods=["POST"])
    def new_user():
        user_details = request.form

        username = user_details.get("username")
        password = user_details.get("password")

        if not username or not password:
            flash("Username or password can't be empty")
            session["signup_username"] = username
            return redirect("/signup")

        repo = UserRepository(get_db())

        user_id = repo.create(User(id=0, username=username, password=password))

        session["user_id"] = user_id
        session["username"] = username

        return redirect("/books")

    @app.route("/login", methods=["GET"])
    def login():
        return render_template("login.html", username=session.pop("login_username", ""))

    @app.route("/sessions", methods=["POST"])
    def new_session():
        user_details = request.form

        username = user_details.get("username")
        password = user_details.get("password")

        if not username or not password:
            flash("Username or password can't be empty")
            session["login_username"] = username
            return redirect("/login")

        repo = UserRepository(get_db())

        user = repo.get_by_username(username)

        if not user or password != user.password:
            flash("Invalid username or password")
            session["login_username"] = username
            return redirect("/login")

        session["user_id"] = user.id
        session["username"] = user.username

        return redirect("/books")

    @app.route("/logout", methods=["GET"])
    def logout():

        session.pop("user_id", None)
        session.pop("username", None)

        flash("Logged out!")

        return redirect("/")

    return app


app = create_app()
