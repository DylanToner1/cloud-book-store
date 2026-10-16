class Book:
    def __init__(self, id: int, title: str, author: str) -> None:
        self.id = id
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        return f"Book({self.id}: {self.title} by {self.author})"
