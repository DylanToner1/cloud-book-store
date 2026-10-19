import os
import threading
from pathlib import Path

import pytest
from werkzeug.serving import make_server
from yoyo import get_backend, read_migrations

from app import create_app
from lib.db_conn import DatabaseConnection

TEST_URL = os.getenv("POSTGRES_TEST_URL", "postgresql://localhost/book_store_test")
MIGRATIONS = Path(__file__).parent.parent / "migrations"


@pytest.fixture(scope="session", autouse=True)
def migrated_db():
    """
    Runs migrations on the test DB once it's ready.
    autouse means it runs every time
    """

    backend = get_backend(TEST_URL)
    migrations = read_migrations(str(MIGRATIONS))

    with backend.lock():  # stop two runs from migrating at the same time
        # apply migrations to test db
        backend.apply_migrations(backend.to_apply(migrations))


@pytest.fixture
def db_connection(migrated_db):
    """
    Connect to the test DB and seed
    """

    conn = DatabaseConnection(TEST_URL)
    conn.connect()
    conn.seed("seeds/books.sql")  # reset data for each test
    return conn


@pytest.fixture(scope="session")
def app(migrated_db):
    """
    Creates a new flask app that uses the test DB
    """

    app = create_app(db_url=TEST_URL)
    app.config["TESTING"] = True
    return app


@pytest.fixture(scope="session")
def base_url(app):
    """
    Starts a test server using the app builder above, which has the test DB.
    Has to be called base_url as that is what playwright looks for.
    binds to port 0, which means a random free port.
    yeilds the generated url and shuts down when the test finishes.
    """

    server = make_server("127.0.0.1", 0, app, threaded=True)  # port 0 means a free port
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.port}"
    server.shutdown()
