from datetime import date

from lib.models.film import Film


def test_film_init():
    film = Film(1, "title", date(2026, 10, 20))

    assert film.id == 1
    assert film.title == "title"
    assert film.release_date == date(2026, 10, 20)


def test_film_eq():
    film = Film(1, "title", date(2026, 10, 20))
    film2 = Film(1, "title", date(2026, 10, 20))

    assert film == film2


def test_film_repr():
    film = Film(1, "title", date(2026, 10, 20))

    assert str(film) == "Film(1: title, released on 2026-10-20)"
