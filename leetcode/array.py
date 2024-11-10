__author__ = "730749614"


def array(original: list[int], m: int, n: int) -> list[list[int]]:
    # m - rows
    # n - columns
    inty: int = 0
    indexy: int = 0
    digi: int = 0
    inner: list[int] = []
    outer: list[int] = []
    while digi < n:
        while inty < m:
            inner.append(original[indexy])
            inty += 1
            indexy += 1
        outer.append(inner)
        digi += 1
        inty = 0
    return outer


print(array([1, 2, 3, 4], 2, 2))
