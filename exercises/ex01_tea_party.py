"""Calculate the number of tea bags needed, treats needed, and the cost for a tea party based on the number of people attending"""

__author__ = "730749614"


def main_planner(guests: int) -> None:
    """returns all the information for the tea party based on the capacity"""
    # have to print out all information using string concatenation and \n to display on separate lines
    print(
        "A Cozy Tea Party for "
        + str(guests)
        + " People!\nTea Bags: "
        + str(tea_bags(people=guests))  # call tea_bags function
        + "\nTreats: "
        + str(treats(people=guests))  # call treats function
        + "\nCost: $"
        + str(
            cost(tea_count=tea_bags(guests), treat_count=treats(guests))
        )  # call cost function
    )


def tea_bags(people: int) -> int:
    """returns the number of tea bags needed for party capacity"""
    # 2 tea bags per person attending
    return people * 2


def treats(people: int) -> int:
    """returns the number of treats needed for party capcity"""
    # 1.5 treats per tea bag needed
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """returns the total cost for tea party"""
    # 50 cents per tea bag and 75 cents per treat
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    """gathers user input for number of people attending and makes code runnable"""
    main_planner(guests=int(input("How many guests are attending your tea party?")))
