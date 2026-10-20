from lib.db_conn import DatabaseConnection
from lib.models.film import Film


class FilmRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection: DatabaseConnection = connection

    # Retrieve all films
    def all(self) -> list[Film]:
        return self._connection.execute("SELECT * from films", cls=Film)

    # Find a single film by their id
    def find(self, film_id):
        rows = self._connection.execute(
            "SELECT * from films WHERE id = %s", [film_id], cls=Film
        )
        return rows[0] if rows else None

    # Create a new film
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, film: Film):
        rows = self._connection.execute(
            "INSERT INTO films (title, release_date) VALUES (%s, %s) RETURNING id",
            [film.title, film.release_date],
        )
        return int(rows[0]["id"])

    # Delete an film by their id
    def delete(self, film_id):
        self._connection.execute("DELETE FROM films WHERE id = %s", [film_id])
