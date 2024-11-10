"""File to define Bear class."""

__author__ = "730749614"


class Bear:
    """Creates Bear Class."""

    age: int
    hunter_score: int

    def __init__(self):
        """Initializes Bear."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Models one day for bear."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish) -> None:
        """Updates hunger score."""
        self.hunger_score += num_fish
