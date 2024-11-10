__author__ = "730749614"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_behavior() -> None:
    """Test that only_evens returns a the correct list of only even integers."""
    listy: list[int] = [5, 10, 8]
    assert only_evens(listy) == [10, 8]


def test_only_evens_mutate() -> None:
    """Tests that the list "a" is not mutated"""
    a: list[int] = [1, 2, 3, 4, 5]
    only_evens(a)
    assert a == [1, 2, 3, 4, 5]


def test_only_evens_edge_case() -> None:
    """Tests that a list of all odd numbers returns an empty list"""
    listy: list[int] = [3, 5, 7]
    assert only_evens(listy) == []


def test_sub_behavior() -> None:
    """Tests that sub returns the correct subset"""
    listy: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(listy, 2, 3) == [3]


def test_sub_mutate():
    """Tests that the list "a" is not mutated at all"""
    a: list[int] = [1, 2, 3, 4, 5]
    sub(a, 1, 4)
    assert a == [1, 2, 3, 4, 5]


def test_sub_edge_case() -> None:
    """Test if sub will return the whole list if start is negative
    and end is larger than the length of the input list"""
    listy: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(listy, -5, 100) == [1, 2, 3, 4, 5, 6]


def test_add_at_index_behavior() -> None:
    """Tests if  add_at_index inserts the integer at the index correctly"""
    list1: list[int] = [1, 2, 3, 5]
    add_at_index(list1, 4, 3)
    assert list1 == [1, 2, 3, 4, 5]


def test_add_at_index_ret_value() -> None:
    """test that add_at _index returns nothing"""
    list1: list[int] = [1, 2, 3, 4]
    assert add_at_index(list1, 1, 2) == None


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    with pytest.raises(IndexError):
        add_at_index([1, 2, 3, 4], 5, 10)
        # an IndexError is raised for the case when the add_at_index is
        # given an <index_to_insert_num>
        # that is greater than the length of our <list_object>
