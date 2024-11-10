__author__ = "730749614"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_behavior() -> None:
    """Tests if find_and_remove function returns the max number from input list"""
    listy: list[int] = [5, 10, 8]
    assert find_and_remove_max(listy) == 10


def test_find_and_remove_max_mut() -> None:
    """Tests if all max values are removed from input list"""
    listy: list[int] = [10, 7, 6, 10, 9]
    find_and_remove_max(listy)
    assert listy == [7, 6, 9]


def test_find_and_remove_edge_case() -> None:
    """ ""Test if input is an empty listy -1 will be returned"""
    listy: list[int] = []
    assert find_and_remove_max(listy) == -1
