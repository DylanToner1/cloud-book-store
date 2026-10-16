from playwright.sync_api import Page, expect
from lib.db_conn import DatabaseConnection


# def test_has_title(page: Page):
#     page.goto("http://127.0.0.1:5001/books")

#     ul = page.get_by_role("listitem")

#     expect(ul).to_have_text(
#         [
#             "The Gruffalo by Julia Donaldson",
#             "Ada Twist, Scientist by Andrea Beaty",
#             "The Girl Who Drank the Moon by Kelly Barnhill",
#             "Dragons in a Bag by Zetta Elliott",
#         ]
#     )


def test_can_add_book(page: Page):
    conn = DatabaseConnection()

    conn.connect()

    conn.seed("seeds/books.sql")

    page.goto("http://127.0.0.1:5001/books")

    page.get_by_label("Title").fill("test book")
    page.get_by_label("Author").fill("test author")

    page.get_by_role("button", name="Submit").click()

    expect(
        page.get_by_role("listitem").filter(has_text="test book by test author")
    ).to_be_visible()
