"""Mutating functions."""

__author__ = "730749614"


def manual_append(listy: list[int], inty: int) -> None:
    listy.append(inty)


a: list[int] = [1, 2, 3]
manual_append(a, 2)
print(a)


def double(listyy: list[int]) -> None:
    idx: int = 0
    while idx < len(listyy):
        listyy[idx] = 2 * listyy[idx]
        idx += 1


a = [1, 2, 3]
double(a)
print(a)

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
