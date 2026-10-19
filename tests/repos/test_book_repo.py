from lib.book_repo import BookRepository
from lib.models.book import Book


def test_get_all_books(db_connection):
    repo = BookRepository(db_connection)

    result = repo.all()

    assert result == [
        Book(1, "The Gruffalo", "Julia Donaldson"),
        Book(2, "Ada Twist, Scientist", "Andrea Beaty"),
        Book(3, "The Girl Who Drank the Moon", "Kelly Barnhill"),
        Book(4, "Dragons in a Bag", "Zetta Elliott"),
    ]


def test_get_single_book(db_connection):
    repo = BookRepository(db_connection)

    result = repo.find(2)

    assert result == Book(2, "Ada Twist, Scientist", "Andrea Beaty")


def test_create_book(db_connection):
    repo = BookRepository(db_connection)

    new_book = Book(0, "test", "test")

    repo.create(new_book)

    result = repo.all()

    assert result == [
        Book(1, "The Gruffalo", "Julia Donaldson"),
        Book(2, "Ada Twist, Scientist", "Andrea Beaty"),
        Book(3, "The Girl Who Drank the Moon", "Kelly Barnhill"),
        Book(4, "Dragons in a Bag", "Zetta Elliott"),
        Book(5, "test", "test"),
    ]


def test_delete_book(db_connection):
    repo = BookRepository(db_connection)

    repo.delete(2)

    result = repo.all()

    assert result == [
        Book(1, "The Gruffalo", "Julia Donaldson"),
        Book(3, "The Girl Who Drank the Moon", "Kelly Barnhill"),
        Book(4, "Dragons in a Bag", "Zetta Elliott"),
    ]
