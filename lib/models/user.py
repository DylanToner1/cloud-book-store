class User:
    def __init__(self, id: int, username: str, password: str) -> None:
        self.id = id
        self.username = username
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        return f"User({self.id}: {self.username})"
