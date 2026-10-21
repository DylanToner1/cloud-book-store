from datetime import date

from lib.film_repo import FilmRepository
from lib.models.film import Film


def test_get_all_films(db_connection):
    repo = FilmRepository(db_connection)

    result = repo.all()

    assert result == [
        Film(1, "title1", date(2026, 10, 20)),
        Film(2, "title2", date(2026, 9, 20)),
        Film(3, "title3", date(2026, 8, 20)),
        Film(4, "title4", date(2026, 7, 20)),
    ]


def test_get_single_film(db_connection):
    repo = FilmRepository(db_connection)

    result = repo.find(2)

    assert result == Film(2, "title2", date(2026, 9, 20))


def test_create_film(db_connection):
    repo = FilmRepository(db_connection)

    new_film = Film(0, "title5", date(2026, 11, 20))

    repo.create(new_film)

    result = repo.all()

    assert result == [
        Film(1, "title1", date(2026, 10, 20)),
        Film(2, "title2", date(2026, 9, 20)),
        Film(3, "title3", date(2026, 8, 20)),
        Film(4, "title4", date(2026, 7, 20)),
        Film(5, "title5", date(2026, 11, 20)),
    ]


def test_delete_film(db_connection):
    repo = FilmRepository(db_connection)

    repo.delete(2)

    result = repo.all()

    assert result == [
        Film(1, "title1", date(2026, 10, 20)),
        Film(3, "title3", date(2026, 8, 20)),
        Film(4, "title4", date(2026, 7, 20)),
    ]
