from lib.models.book import Book
from lib.db_conn import DatabaseConnection


class BookRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection: DatabaseConnection = connection

    # Retrieve all books
    def all(self) -> list[Book]:
        return self._connection.execute("SELECT * from books", cls=Book)

    # Find a single book by their id
    def find(self, book_id):
        rows = self._connection.execute(
            "SELECT * from books WHERE id = %s", [book_id], cls=Book
        )
        return rows[0] if rows else None

    # Create a new book
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, book):
        rows = self._connection.execute(
            "INSERT INTO books (title, author) VALUES (%s, %s) RETURNING id",
            [book.title, book.author],
        )
        return int(rows[0]["id"])

    # Delete an book by their id
    def delete(self, book_id):
        self._connection.execute("DELETE FROM books WHERE id = %s", [book_id])
