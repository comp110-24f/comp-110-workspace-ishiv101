__author__ = "730749614"


def input_guess(secret_word_len: int) -> str:
    """checks if the guessed word is the same length as the secret word"""
    # important - will prompt user to try again if not the right length
    # used in main functions
    user_word: str = input(f"Enter a {secret_word_len} character word: ")
    while len(user_word) != secret_word_len:  # Loops until input is correct length
        user_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return user_word  # Once out of while loop return user_word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """checks if a character is in the secret word"""
    # will be used to return a colored square in the next function
    assert len(char_guess) == 1
    counter: int = 0
    while counter < len(secret_word):
        # Loops through each char in secret_word to see if it matches char_guess
        if secret_word[counter] == char_guess:
            return True
        else:
            counter += 1
    return False  # If no characters match at the end of the loop return False


def emojified(guess: str, word: str) -> str:
    """returns a string of emoji boxes based on the word guessed"""
    # prints white box if character is not present, yellow box if character is present
    # but not in right place, green box if charcter is present and in the right space
    assert len(guess) == len(word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    empty: str = ""
    num: int = 0
    while num < len(word):
        if guess[num] == word[num]:
            # checks if letter in the same place and puts green box
            empty += GREEN_BOX
        elif contains_char(secret_word=word, char_guess=guess[num]):
            # check if letter is in secret word and puts yellow box
            empty += YELLOW_BOX
        else:
            # if letter is not in the word at all it adds white box
            empty += WHITE_BOX
        num += 1
    return empty


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # important - calls input_guess to ask for user entry
    # impotant - To return try again if length is wrong
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess=guess, word=secret))
        if emojified(guess=guess, word=secret) == "\U0001F7E9" * len(secret):
            print(f"You won in {turn}/6 turns!")
            # if user guesses word correctly game ends
            break
        else:
            turn += 1
    else:
        print("X/6 - Sorry, try again tomorrow!")
    # if user does not guess in 6 guesses, game ends


if __name__ == "__main__":
    main(secret="codes")
