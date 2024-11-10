from lessons.quiz02_prac.unit_test_prac.functions import find_even, add_key_to_dicts


def test_find_even_use_case() -> None:
    listy: list[int] = [1, 3, 5, 6, 7, 8, 9]
    assert find_even(listy) == 3


def test_add_key_to_dict() -> None:
    dicty: list[dict] = [{"red": 1}, {"orange": 2}]
    add_key_to_dicts(dicty, "yellow", 3)
    assert dicty == [{"red": 1, "yellow": 3}, {"orange": 2, "yellow": 3}]
