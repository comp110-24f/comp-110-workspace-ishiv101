__author__ = "730749614"


def num_instances(phrase: str, search_char: str) -> int:
    """returns the instances of a character in a phrase"""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if search_char == phrase[index]:
            count += 1
        index += 1
    return count


print(num_instances("football", "o"))
