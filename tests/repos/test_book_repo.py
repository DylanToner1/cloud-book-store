from lib.book_repo import BookRepository
from lib.models.book import Book
from decimal import Decimal


def test_get_all_books(db_connection):
    repo = BookRepository(db_connection)

    result = repo.all()

    assert result == [
        Book(1, "The Gruffalo", "Julia Donaldson", None, Decimal("2.3"), None),
        Book(2, "Ada Twist, Scientist", "Andrea Beaty", None, Decimal("4.6"), None),
        Book(
            3,
            "The Girl Who Drank the Moon",
            "Kelly Barnhill",
            None,
            Decimal("1.2"),
            None,
        ),
        Book(4, "Dragons in a Bag", "Zetta Elliott", None, Decimal("5.0"), None),
    ]


def test_get_single_book(db_connection):
    repo = BookRepository(db_connection)

    result = repo.find(2)

    assert result == Book(
        2, "Ada Twist, Scientist", "Andrea Beaty", None, Decimal("4.6"), None
    )


def test_create_book(db_connection):
    repo = BookRepository(db_connection)

    new_book = Book(0, "test", "test", None, Decimal("1.7"), None)

    repo.create(new_book)

    result = repo.all()

    assert result == [
        Book(1, "The Gruffalo", "Julia Donaldson", None, Decimal("2.3"), None),
        Book(2, "Ada Twist, Scientist", "Andrea Beaty", None, Decimal("4.6"), None),
        Book(
            3,
            "The Girl Who Drank the Moon",
            "Kelly Barnhill",
            None,
            Decimal("1.2"),
            None,
        ),
        Book(4, "Dragons in a Bag", "Zetta Elliott", None, Decimal("5.0"), None),
        Book(5, "test", "test", None, Decimal("1.7"), None),
    ]


def test_delete_book(db_connection):
    repo = BookRepository(db_connection)

    repo.delete(2)

    result = repo.all()

    assert result == [
        Book(1, "The Gruffalo", "Julia Donaldson", None, Decimal("2.3"), None),
        Book(
            3,
            "The Girl Who Drank the Moon",
            "Kelly Barnhill",
            None,
            Decimal("1.2"),
            None,
        ),
        Book(4, "Dragons in a Bag", "Zetta Elliott", None, Decimal("5.0"), None),
    ]
