from lib.models.user import User
from lib.user_repo import UserRepository


def test_get_all_users(db_connection):
    repo = UserRepository(db_connection)

    result = repo.all()

    assert result == [
        User(1, "test", "test"),
        User(2, "test2", "test2"),
    ]


def test_get_single_user_by_id(db_connection):
    repo = UserRepository(db_connection)

    result = repo.get_by_id(2)

    assert result == User(2, "test2", "test2")


def test_get_single_user_by_username(db_connection):
    repo = UserRepository(db_connection)

    result = repo.get_by_username("test")

    assert result == User(1, "test", "test")


def test_create_user(db_connection):
    repo = UserRepository(db_connection)

    new_user = User(0, "test3", "test3")

    repo.create(new_user)

    result = repo.all()

    assert result == [
        User(1, "test", "test"),
        User(2, "test2", "test2"),
        User(3, "test3", "test3"),
    ]


def test_delete_user(db_connection):
    repo = UserRepository(db_connection)

    repo.delete(2)

    result = repo.all()

    assert result == [
        User(1, "test", "test"),
    ]
