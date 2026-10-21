from lib.models.user import User
from lib.user_repo import UserRepository

# passwords are test, test2
# hashes must match the seed file
TEST1_PW_HASH = "$2b$12$AvvLEFFUG/00XzBB6Xz54Onm9cTnqJQ7TIf5Xm4JqDErb7TaAyXJi"
TEST2_PW_HASH = "$2b$12$z4ddsyuIeQpdlHZ3fjAkM.GmR8oHF6GI77YbfQJdI4g7gjX9jVGIC"


def test_get_all_users(db_connection):
    repo = UserRepository(db_connection)

    result = repo.all()

    assert result == [
        User(1, "test", TEST1_PW_HASH),
        User(2, "test2", TEST2_PW_HASH),
    ]


def test_get_single_user_by_id(db_connection):
    repo = UserRepository(db_connection)

    result = repo.get_by_id(2)

    assert result == User(2, "test2", TEST2_PW_HASH)


def test_get_single_user_by_username(db_connection):
    repo = UserRepository(db_connection)

    result = repo.get_by_username("test")

    assert result == User(1, "test", TEST1_PW_HASH)


def test_create_user(db_connection):
    repo = UserRepository(db_connection)

    new_user = User(0, "test3", "test3")

    repo.create(new_user)

    result = repo.all()

    assert result == [
        User(1, "test", TEST1_PW_HASH),
        User(2, "test2", TEST2_PW_HASH),
        User(3, "test3", "test3"),
    ]


def test_delete_user(db_connection):
    repo = UserRepository(db_connection)

    repo.delete(2)

    result = repo.all()

    assert result == [
        User(1, "test", TEST1_PW_HASH),
    ]
