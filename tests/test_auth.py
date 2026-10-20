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


def test_user_log_in_page_wrong_credentials(db_connection, page: Page):
    page.goto("/login")

    page.get_by_label("Username").fill("wrong")
    page.get_by_label("Password").fill("wrong")

    page.get_by_role("button", name="Log In").click()
    assert page.url.endswith("/login")

    expect(
        page.locator("p.error").filter(has_text="Invalid username or password")
    ).to_be_visible()

    expect(page.get_by_label("Username")).to_have_value("wrong")
    expect(page.get_by_label("Password")).to_be_empty()


def test_user_log_in_page_invalid_input(db_connection, page: Page):
    page.goto("/login")

    page.get_by_label("Username").fill("test")
    page.get_by_label("Password").fill("")

    page.get_by_role("button", name="Log In").click()
    assert page.url.endswith("/login")

    expect(
        page.locator("p.error").filter(has_text="Username or password can't be empty")
    ).to_be_visible()

    expect(page.get_by_label("Username")).to_have_value("test")
    expect(page.get_by_label("Password")).to_be_empty()


def test_user_sign_up_page_invalid_input(db_connection, page: Page):
    page.goto("/signup")

    page.get_by_label("Username").fill("test")
    page.get_by_label("Password").fill("")

    page.get_by_role("button", name="Sign Up").click()
    assert page.url.endswith("/signup")

    expect(
        page.locator("p.error").filter(has_text="Username or password can't be empty")
    ).to_be_visible()

    expect(page.get_by_label("Username")).to_have_value("test")
    expect(page.get_by_label("Password")).to_be_empty()


def test_user_log_out_page(logged_in_page):
    page = logged_in_page

    page.get_by_role("link", name="Log Out").click()

    expect(page.locator("p.success").filter(has_text="Logged out!")).to_be_visible()

    # make sure they have actually been logged out, shouldn't be able to access the new book page
    page.goto("/books/new")

    assert page.url.endswith("/login")
