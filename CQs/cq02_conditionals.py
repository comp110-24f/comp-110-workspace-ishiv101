"""Checks if the number the user guessed is the secret number."""

__author__ = "730749614"


def guess_a_number() -> None:
    """checks if user guesses the correct secret number"""
    secret: int = 7
    x: str = input("Guess a number: ")
    print("Your guess was " + x)
    if int(x) == secret:
        print("You got it!")
    elif int(x) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
