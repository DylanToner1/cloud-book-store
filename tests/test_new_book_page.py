from playwright.sync_api import Page, expect
from lib.db_conn import DatabaseConnection


def test_can_add_book(logged_in_page: Page):
    page = logged_in_page

    page.goto("/books/new")

    page.get_by_label("Title").fill("test book")
    page.get_by_label("Author").fill("test author")
    page.get_by_label("Rating").fill("2.3")

    page.get_by_role("button", name="Submit").click()

    expect(
        page.get_by_role("listitem").filter(has_text="test book by test author | 2.3/5")
    ).to_be_visible()


def test_cant_add_book_blank_values(logged_in_page: Page):
    page = logged_in_page

    page.goto("/books/new")

    page.get_by_label("Title").fill("")
    page.get_by_label("Author").fill("test author")

    page.get_by_role("button", name="Submit").click()

    expect(
        page.locator("p.error").filter(has_text="Title or Author can't be blank!")
    ).to_be_visible()

    expect(page.get_by_role("listitem").filter(has_text="test author")).to_have_count(0)


def test_unauthenticated_cant_add_book(db_connection, page: Page):

    page.goto("/books/new")

    assert page.url.endswith("/login")
