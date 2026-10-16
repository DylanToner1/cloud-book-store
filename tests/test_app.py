from lib.app import app


def test_get_books_returns_a_200():
    client = app.test_client()

    response = client.get("/books")

    assert response.status_code == 200


def test_get_authors_returns_200():
    client = app.test_client()

    resp = client.get("/authors")

    assert resp.status_code == 200


def test_get_authors_returns_all_authors():
    client = app.test_client()

    resp = client.get("/authors")

    assert resp.json == [
        {"name": "Julia Donaldson", "dob": "1948-09-16"},
        {"name": "Andrea Beaty", "dob": "1961-10-08"},
        {"name": "Kelly Barnhill", "dob": "1973-01-01"},
        {"name": "Zetta Elliott", "dob": "1979-11-11"},
    ]
