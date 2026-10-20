from playwright.sync_api import Page, expect
from lib.db_conn import DatabaseConnection


def test_books_visible(db_connection, page: Page):
    page.goto("/books")

    expect(
        page.get_by_role("listitem").filter(
            has_text="The Gruffalo by Julia Donaldson | 2.3/5"
        )
    ).to_be_visible()
