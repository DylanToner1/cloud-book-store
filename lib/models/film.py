from datetime import date


class Film:
    def __init__(self, id: int, title: str, release_date: date) -> None:
        self.id = id
        self.title = title
        self.release_date = release_date

    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__

    def __repr__(self) -> str:
        return f"Film({self.id}: {self.title}, released on {self.release_date.isoformat()})"
