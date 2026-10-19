from lib.models.user import User


def test_user_creation():
    user = User(1, "test", "test")

    assert user.id == 1
    assert user.username == "test"
    assert user.password == "test"


def test_user_eq():
    user = User(1, "test", "test")
    user2 = User(1, "test", "test")

    assert user == user2


def test_user_repr():
    user = User(1, "test", "test")

    assert str(user) == "User(1: test)"
