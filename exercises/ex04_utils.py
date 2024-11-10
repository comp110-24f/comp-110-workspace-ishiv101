def all(listy: list[int], inty: int) -> bool:
    """checks if the list of ints consists of only that int given as a parameter"""
    idx: int = 0
    count: int = 0
    while idx < len(listy):
        if inty == listy[idx]:
            count += 1
        idx += 1
    if len(listy) == 0:
        # if list is empy return False
        return False
    elif count == len(listy):
        # if list is all that integer print True
        return True
    else:
        return False


def max(listy: list[int]) -> int:
    """returns the max number in the list"""
    first: int = listy[0]
    for item in listy:
        if item > first:
            first = item  # changes the value of the max number
    return first  # max number


def is_equal(listy1: list[int], listy2: list[int]) -> bool:
    """checks if two lists are exactly the same"""
    if len(listy1) != len(listy2):
        # if lists are different lengths then return False
        return False
    idx: int = 0
    while idx < len(listy1) and idx < len(listy2):
        if listy1[idx] == listy2[idx]:
            idx += 1  # checks every index
        else:
            return False  # if index is not the same returns False and stops
    return True  # if eveery index is the same return True


def extend(listy1: list[int], listy2: list[int]) -> None:
    """will add the second list to the end of the first list"""
    for item in listy2:
        listy1.append(item)
        # does not return or print anything
