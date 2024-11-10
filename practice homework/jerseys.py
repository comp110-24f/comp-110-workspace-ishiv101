def greet(name: str) -> None:
    print(
        "Hello "
        + name
        + ", your name starts with an "
        + name[0]
        + " and ends with an "
        + name[len(name) - 1]
    )


def main() -> None:
    (greet(name="Molly"))

    # Example usage:


main()
