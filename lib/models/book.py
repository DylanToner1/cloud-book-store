from decimal import Decimal


class Book:
    def __init__(
        self,
        id: int,
        title: str,
        author: str,
        synopsis: str | None,
        rating: Decimal | None,
        notes: str | None,
    ) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.synopsis = synopsis
        self.rating = rating
        self.notes = notes

    def format_rating(self):
        if self.rating:
            return f"{self.rating}/5"

        return "no rating"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        return (
            f"Book({self.id}: {self.title} by {self.author} | {self.format_rating()})"
        )
