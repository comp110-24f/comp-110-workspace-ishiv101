__author__ = "730749614"


def invert(dicty: dict[str, str]) -> dict[str, str]:
    """swaps the positions of each key with its corresponding value"""
    empty: dict[str, str] = {}
    # take the input from parameter and puts it in new dict to return
    for k in dicty:
        for j in dicty:
            # double for loop to compare each value to eachother
            # duplicate values with cause duplicate keys when inverted - not allowed
            if k != j and dicty[k] == dicty[j]:
                raise KeyError(
                    "If inverted then duplicate keys will occur which is NOT allowed"
                )
        # swaps the values and keys
        value: str = dicty[k]
        empty[value] = k
    return empty


def favorite_color(dicty: dict[str, str]) -> str:
    """will return the most frequent color in the input dictionary"""
    color: str = ""
    # variable to count up how many of each color there is
    count: int = 0
    empty: dict[str, int] = {}
    # create another dictionary (key = color(cannot have duplicates)
    # value = frequency of each color(can have duplicates))
    for k in dicty:
        color = dicty[k]
        # count has to start at 0 every time
        count = 0
        for j in dicty:
            if dicty[j] == color:
                count += 1
        empty[color] = count

    max: int = 0  # will find the highest value number in empty dict (max)
    max_color: str = ""  # will return the color name with highest value
    for k in empty:
        if empty[k] > max:
            max_color = k
            max = empty[k]
    return max_color  # will return most frequent color (favorite color)


def count(listy: list[str]) -> dict[str, int]:
    """counts how many times each value in the input list appears"""
    empty: dict[str, int] = {}
    # create empty dict to return
    for word in listy:
        if word in empty:  # if word already in empty
            empty[word] += 1
        else:  # if word not in empty yet than add a key for it
            empty[word] = 1  # starts as 1 to count first instance a word is seen
    return empty


def alphabetizer(listy: list[str]) -> dict[str, list[str]]:
    """create a dictionary where key = each unqiue starting letter from input list,
    value = every word that starts with that letter"""
    empty: dict[str, list[str]] = {}
    for word in listy:  # iterate through each word in input lsit
        if word.lower()[0] in empty:
            # if letter already in dict than just add a word that starts with
            # that letter to its value
            empty[word.lower()[0]].append(word)
        else:
            # if letter not in dict add it as a key and value equals the first
            # word starting with that letter
            empty[word.lower()[0]] = [word]
    return empty


def update_attendance(dicty: dict[str, list[str]], day: str, student: str) -> None:
    """will mutuate the input dictionary to update when a students shows up to
    class on what day of the week"""
    if day in dicty:  # if day already in dict add student to already created value
        if student not in dicty[day]:
            dicty[day].append(student)
    else:  # if day not in dict then create a new key
        dicty[day] = [student]
