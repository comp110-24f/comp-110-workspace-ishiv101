"""File to define Fish class."""

__author__ = "730749614"


class Fish:
    """Creates Fish Class."""

    age: int

    def __init__(self):
        """Initializes Fish."""
        self.age = 0
        return None

    def one_day(self):
        """Ages Fish."""
        self.age += 1
        return None
