from playwright.sync_api import Page, expect


def test_books_visible(db_connection, page: Page):
    page.goto("/books")

    expect(
        page.get_by_test_id("book-title").filter(has_text="The Gruffalo")
    ).to_be_visible()

    expect(
        page.get_by_test_id("book-author").filter(has_text="by Julia Donaldson")
    ).to_be_visible()

    expect(
        page.get_by_test_id("book-rating").filter(has_text="Rating: 2.3/5")
    ).to_be_visible()
