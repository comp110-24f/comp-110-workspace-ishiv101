__author__ = "730749614"


def only_evens(listy: list[int]) -> list[int]:
    """returns a list of only even integers from the input list"""
    empty: list[int] = []
    for num in listy:
        # iterates through each number in input list
        if num % 2 == 0:
            # modulo to check if number is even
            empty.append(num)
    return empty


def sub(listy: list[int], start: int, end: int) -> list[int]:
    """returns a subset of the input list from the starting parameter index (inclusive)
    to the ending parameter index (exclusive)"""
    empty: list[int] = []
    # if starting index is out of bounds
    if start < 0:
        start = 0
    elif start >= len(listy):
        return empty
    # if ending index is out of bounds
    if end > len(listy):
        end = len(listy)
    elif end <= 0:
        return empty
    # creates the subset
    for index in range(start, end):
        empty.append(listy[index])
    return empty


def add_at_index(listy: list[int], inty: int, indexy: int) -> None:
    """inserts the parameter inty at parameter indexy in input list"""
    # if there is an error at specified index in list then no output, raise error
    if indexy < 0 or indexy > len(listy):
        raise IndexError("Index is out of bounds for the input list")
    # first element needed to increase size so rest follow at the correct index
    listy.append(0)
    # moves each element one to the right
    prev: int = inty
    for i in range(indexy, len(listy)):
        curr: int = listy[i]
        listy[i] = prev
        prev = curr
