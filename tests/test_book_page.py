from playwright.sync_api import Page, expect
from lib.db_conn import DatabaseConnection


def test_book_exists(db_connection, page: Page):
    page.goto("/books/1")

    expect(
        page.get_by_test_id("book-title").filter(has_text="The Gruffalo")
    ).to_be_visible()

    expect(
        page.get_by_test_id("book-author").filter(has_text="by Julia Donaldson")
    ).to_be_visible()

    expect(
        page.get_by_test_id("book-rating").filter(has_text="Rating: 2.3/5")
    ).to_be_visible()


def test_book_doesnt_exist(db_connection, page: Page):
    page.goto("/books/99")

    assert page.url.endswith("/books")

    expect(
        page.locator("p.error").filter(has_text="That book doesn't exist!")
    ).to_be_visible()
