from lib.models.book import Book


def test_book_creation():
    book = Book(1, "title", "author")

    assert book.id == 1
    assert book.title == "title"
    assert book.author == "author"


def test_book_eq():
    book = Book(1, "title", "author")
    book2 = Book(1, "title", "author")

    assert book == book2


def test_book_repr():
    book = Book(1, "title", "author")

    assert str(book) == "Book(1: title by author)"
