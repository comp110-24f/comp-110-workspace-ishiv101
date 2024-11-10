__author__ = "730749614"


def find_and_remove_max(listy: list[int]) -> int:
    max: int = -1
    # Assume the first element is the maximum
    index: int = 0
    if listy == []:
        # Return -1 if the list is empty
        return max
    else:
        # Uses while loop to find max value in input list
        while index < len(listy):
            if listy[index] > max:
                max = listy[index]
            index += 1

    # Remove all instances of the max value using .pop()
    i = 0
    while i < len(listy):
        if listy[i] == max:
            listy.pop(i)  # Remove the element at index i
        else:
            i += 1  # Only increment if no pop, to avoid skipping elements

    return max
