import os
from datetime import date
from decimal import Decimal

from dotenv import load_dotenv
from flagsmith import Flagsmith
from flask import Flask, current_app, flash, redirect, render_template, request, session
from flask_bcrypt import Bcrypt

from auth import login_required
from lib.book_repo import BookRepository
from lib.db_conn import DatabaseConnection
from lib.film_repo import FilmRepository
from lib.models.book import Book
from lib.models.film import Film
from lib.models.user import User
from lib.user_repo import UserRepository

load_dotenv()


def get_db():
    # builds a database connection from the configured database url
    conn = DatabaseConnection(current_app.config["DB_URL"])
    conn.connect()
    return conn


def create_app(db_url=None):
    app = Flask(__name__)

    bcrypt = Bcrypt(app)

    flagsmith = Flagsmith(
        environment_key=os.getenv("FLAGSMITH_KEY"),
    )

    # the app uses whatever database we give it when starting
    app.config["DB_URL"] = db_url or os.getenv(
        "POSTGRES_URL", f"postgresql://localhost/{DatabaseConnection.DATABASE_NAME}"
    )

    app.secret_key = "some_really_secret_key"

    @app.route("/", methods=["GET"])
    def index():
        flags = flagsmith.get_environment_flags()

        show_button = flags.is_feature_enabled("show_demo_button")
        return render_template("index.html", show_button=show_button)

    @app.route("/books", methods=["GET"])
    def books():
        repo = BookRepository(get_db())

        books = repo.all()

        return render_template("books.html", books=books)

    @app.route("/films", methods=["GET"])
    def films():
        repo = FilmRepository(get_db())

        films = repo.all()

        return render_template("films.html", films=films)

    @app.route("/films/new", methods=["GET"])
    @login_required
    def add_film_page():
        return render_template("addfilm.html")

    @app.route("/films/new", methods=["POST"])
    @login_required
    def create_film():
        film_details = request.form

        title = film_details.get("title")
        release_date = film_details.get("release-date")

        if not title or not release_date:
            flash("Title or Release Date can't be blank!")
            return redirect("/films/new")

        release_date = date.fromisoformat(release_date)

        repo = FilmRepository(get_db())

        repo.create(
            Film(
                id=0,
                title=title,
                release_date=release_date,
            )
        )
        return redirect("/films")

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

    @app.route("/books/<id>")
    def get_book(id):
        repo = BookRepository(get_db())

        book = repo.find(id)

        if not book:
            flash("That book doesn't exist!")
            return redirect("/books")

        return render_template("book.html", book=book)

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

        pw_hash = bcrypt.generate_password_hash(password).decode("utf-8")

        repo = UserRepository(get_db())

        user_id = repo.create(User(id=0, username=username, password=pw_hash))

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

        if not user or not bcrypt.check_password_hash(user.password, password):
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
