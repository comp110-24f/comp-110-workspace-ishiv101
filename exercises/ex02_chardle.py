"""EX02 - Chardle - a cute step towards Wordle"""

__author__ = "730749614"


def input_word() -> str:
    user_word: str = input("Enter a 5-character word: ")
    if len(user_word) == 5:
        # user input has to be 5 characters long
        return user_word
    else:
        print("Error: Word must contain 5 characters.")
        # code will just stop if not 5 characters long
        exit()


def input_letter() -> str:
    user_letter: str = input("Enter a single character: ")
    if len(user_letter) == 1:
        # user input has to be 1 character long
        return user_letter
    else:
        print("Error: Character must be a single character.")
        # code will just stop if user input is not 1 character long
        exit()


def contains_char(word: str, letter: str) -> None:
    """Searches for letter in word"""
    print("Searching for " + letter + " in " + word)
    # use multiple if loops to iterate through a finite number of indexes (5 indexes)
    counter: int = 0
    # counter variable counts the number of instances of a particular letter in the word
    if letter == word[0]:
        print(letter + " found at index 0")
        counter += 1
    if letter == word[1]:
        print(letter + " found at index 1")
        counter += 1
    if letter == word[2]:
        print(letter + " found at index 2")
        counter += 1
    if letter == word[3]:
        print(letter + " found at index 3")
        counter += 1
    if letter == word[4]:
        print(letter + " found at index 4")
        counter += 1
    if counter > 1:
        # grammar - instance vs instances
        print(str(counter) + " instances of " + letter + " found in " + word)
    elif counter == 1:
        print(str(counter) + " instance of " + letter + " found in " + word)
    else:
        # counter == 0
        print("No instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
