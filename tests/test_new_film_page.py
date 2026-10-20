from playwright.sync_api import Page, expect
from lib.db_conn import DatabaseConnection


def test_can_add_film(logged_in_page: Page):
    page = logged_in_page

    page.goto("/films/new")

    page.get_by_label("Title").fill("test film")
    page.get_by_label("Release Date").fill("2026-12-31")

    page.get_by_role("button", name="Submit").click()

    expect(
        page.get_by_test_id("film-title").filter(has_text="test film")
    ).to_be_visible()

    expect(
        page.get_by_test_id("film-release_date").filter(has_text="2026-12-31")
    ).to_be_visible()


def test_cant_add_film_blank_values(logged_in_page: Page):
    page = logged_in_page

    page.goto("/films/new")

    page.get_by_label("Title").fill("")
    page.get_by_label("Release Date").fill("2026-12-31")

    page.get_by_role("button", name="Submit").click()

    expect(
        page.locator("p.error").filter(has_text="Title or Release Date can't be blank!")
    ).to_be_visible()

    expect(
        page.get_by_test_id("film-release_date").filter(has_text="2026-12-31")
    ).to_have_count(0)


def test_unauthenticated_cant_add_film(db_connection, page: Page):

    page.goto("/films/new")

    assert page.url.endswith("/login")
