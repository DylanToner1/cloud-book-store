from playwright.sync_api import Page, expect


def test_user_log_in_correct_credentials(app, db_connection):
    client = app.test_client()

    resp = client.post("/sessions", data={"username": "test", "password": "test"})

    assert resp.status_code == 302  # redirects after login
    assert resp.headers["Location"].endswith("/books")


def test_user_log_in_incorrect_credentials(app, db_connection):
    client = app.test_client()

    resp = client.post("/sessions", data={"username": "wrong", "password": "wrong"})

    assert resp.status_code == 302  # redirects back to login page
    assert resp.headers["Location"].endswith("/login")


def test_user_log_in_page(db_connection, page: Page):
    page.goto("/login")

    page.get_by_label("Username").fill("test")
    page.get_by_label("Password").fill("test")

    page.get_by_role("button", name="Log In").click()

    assert page.url.endswith("/books")


def test_user_log_in_page_failed(db_connection, page: Page):
    page.goto("/login")

    page.get_by_label("Username").fill("wrong")
    page.get_by_label("Password").fill("wrong")

    page.get_by_role("button", name="Log In").click()
    assert page.url.endswith("/login")
