from decimal import Decimal

from lib.models.book import Book


def test_book_creation():
    book = Book(1, "title", "author", "synopsis", Decimal("4.2"), "notes")

    assert book.id == 1
    assert book.title == "title"
    assert book.author == "author"
    assert book.synopsis == "synopsis"
    assert book.rating == Decimal("4.2")
    assert book.notes == "notes"


def test_book_eq():
    book = Book(1, "title", "author", "synopsis", Decimal("4.2"), "notes")
    book2 = Book(1, "title", "author", "synopsis", Decimal("4.2"), "notes")

    assert book == book2


def test_book_repr():
    book = Book(1, "title", "author", "synopsis", Decimal("4.2"), "notes")

    assert str(book) == "Book(1: title by author | 4.2/5)"


def test_book_format_rating():
    book = Book(1, "title", "author", "synopsis", Decimal("4.2"), "notes")

    assert book.format_rating() == "4.2/5"

    book.rating = None

    assert book.format_rating() == "no rating"
