from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("/")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Welcome to Book Store")
