__author__ = "730749614"


def string_sum(s: str, k: int) -> int:
    """returns the sum of the digits k times after the input string is
    converted to digits based on the letters alphabetical postion"""
    # first step - convert letter to digits using ord() (ex. z = 26, b = 2)
    empty: str = ""
    for char in s:
        empty = empty + str(ord(char) - 96)
        # s = zbax -> empty = 262124
    # add the digits of the number of empty k times
    i: int = 0
    start: int = 0
    # while loops to repeat step k times
    while i < k:
        start: int = 0
        for digi in empty:
            start += int(digi)
        i += 1
        empty = str(start)
    return start


print(string_sum("iiii", 1))
