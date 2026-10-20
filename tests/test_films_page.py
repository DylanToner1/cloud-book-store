from playwright.sync_api import Page, expect
from lib.db_conn import DatabaseConnection


def test_films_visible(db_connection, page: Page):
    page.goto("/films")

    expect(
        page.get_by_test_id("film-title").filter(has_text="title1")
    ).to_be_visible()

    expect(
        page.get_by_test_id("film-release_date").filter(has_text="2026-10-20")
    ).to_be_visible()
