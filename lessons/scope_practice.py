"""some scope examples"""


def remove_chars(msg: str, char: str) -> str:
    """returns a copy of msg with all instances of char removed"""
    copy: str = ""  # set up an empty string to copy values over
    idx = 0
    while idx < len(msg):
        if msg[idx] != char:
            copy += msg[idx]
        idx += 1

    return copy


word: str = "yoyo"

print(remove_chars(word, "y"))
print(remove_chars(word, "o"))
print(remove_chars("football", "o"))
