import os

import psycopg
from psycopg.rows import class_row, dict_row


class DatabaseConnection:
    DATABASE_NAME = "book_store"

    def __init__(self, url=None):
        self.url = url or f"postgresql://localhost/{self.DATABASE_NAME}"
        self.connection = None

    # This method connects to PostgreSQL using the psycopg library. We connect
    # to localhost and select the database name given in argument.
    def connect(self):
        try:
            self.connection = psycopg.connect(self.url, row_factory=dict_row)
        except psycopg.OperationalError:
            raise Exception(
                f"Couldn't connect to the database {self.DATABASE_NAME}! "
                f"Did you create it using `createdb {self.DATABASE_NAME}`?"
            )

    # This method seeds the database with the given SQL file.
    # We use it to set up our database ready for our tests or application.
    def seed(self, sql_filename):
        self._check_connection()
        if not os.path.exists(sql_filename):
            raise Exception(f"File {sql_filename} does not exist")
        with self.connection.cursor() as cursor:
            cursor.execute(open(sql_filename, "r").read())
            self.connection.commit()

    # This method executes an SQL query on the database.
    # It allows you to set some parameters too. You'll learn about this later.
    def execute(self, query, params=[], cls=None):
        self._check_connection()
        row_factory = class_row(cls) if cls else dict_row

        with self.connection.cursor(row_factory=row_factory) as cursor:
            cursor.execute(query, params)
            if cursor.description is not None:
                result = cursor.fetchall()
            else:
                result = None
            self.connection.commit()
            return result

    CONNECTION_MESSAGE = (
        ""
        "DatabaseConnection.exec_params: Cannot run a SQL query as "
        "the connection to the database was never opened. Did you "
        "make sure to call first the method DatabaseConnection.connect` "
        "in your app.py file (or in your tests)?"
    )

    # This private method checks that we're connected to the database.
    def _check_connection(self):
        if self.connection is None:
            raise Exception(self.CONNECTION_MESSAGE)
