from lib.db_conn import DatabaseConnection
from lib.models.user import User


class UserRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection: DatabaseConnection = connection

    # Retrieve all users
    def all(self) -> list[User]:
        return self._connection.execute("SELECT * from users", cls=User)

    # Find a single user by their id
    def get_by_id(self, user_id) -> User | None:
        rows = self._connection.execute(
            "SELECT * from users WHERE id = %s", [user_id], cls=User
        )
        return rows[0] if rows else None

    def get_by_username(self, username) -> User | None:
        rows = self._connection.execute(
            "SELECT * from users WHERE username = %s", [username], cls=User
        )
        return rows[0] if rows else None

    # Create a new user
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, user: User):
        rows = self._connection.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id",
            [user.username, user.password],
        )
        return int(rows[0]["id"])

    # Delete an user by their id
    def delete(self, user_id):
        self._connection.execute("DELETE FROM users WHERE id = %s", [user_id])
