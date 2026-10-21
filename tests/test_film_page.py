from playwright.sync_api import Page, expect


def test_film_exists(db_connection, page: Page):
    page.goto("/films/1")

    expect(page.get_by_test_id("film-title").filter(has_text="title1")).to_be_visible()

    expect(
        page.get_by_test_id("film-release_date").filter(has_text="2026-10-20")
    ).to_be_visible()


def test_film_doesnt_exist(db_connection, page: Page):
    page.goto("/films/99")

    assert page.url.endswith("/films")

    expect(
        page.locator("p.error").filter(has_text="That film doesn't exist!")
    ).to_be_visible()
