def check_first_letter(word: str, letter: str) -> str:
    """checks if letter is first character of word"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
print(check_first_letter(word="happy", letter="s"))
