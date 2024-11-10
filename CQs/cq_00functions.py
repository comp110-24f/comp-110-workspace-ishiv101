__author__ = "730749614"


def mimic(message: str) -> str:
    """function that mimics back what you say"""
    return message


def main() -> None:
    """Give the result of mimic function"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
