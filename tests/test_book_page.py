from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001/books")

    ul = page.get_by_role("listitem")

    expect(ul).to_have_text(
        [
            "The Gruffalo by Julia Donaldson",
            "Ada Twist, Scientist by Andrea Beaty",
            "The Girl Who Drank the Moon by Kelly Barnhill",
            "Dragons in a Bag by Zetta Elliott",
        ]
    )
