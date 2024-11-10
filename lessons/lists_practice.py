"""Basic Syntac of lists"""

names: list[str]
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

my_name: str = ""  # literal
my_name: str = str()  # constructor

print(my_numbers)

"""adding an item to a list"""
my_numbers.append(1.5)
my_numbers.append(2.3)


print(my_numbers)

"""create an already populated list"""
game_points: list[int] = [102, 86, 94]

"""Subscription Notation/indexing"""
print(game_points[2])
last_game: int = game_points[2]
print(last_game)
print([0, 1, 2][0])

"""modifying by index because lists are mutable"""
game_points[1] = 82
print(game_points)

# cannot modify indexes with strings
x: str = "110"
# x[0] = 2 (does not work)

"""Getting the length of list"""
print(len(game_points))
y: int = len(game_points)
print(y)

"""remove an element at the index"""
game_points.pop(1)
print(game_points.pop(1))
print(game_points)

"""duplicate values in list"""
grocery_list: list[str] = ["bananas", "milk", "eggs"]
grocery_list.append("bananas")
print(grocery_list)


# Write a function called display
# Input: list[int]
# Return Value: None
# Loop over the input a print every value
# Try calling it on game_points


def display(listy: list[int]) -> None:
    idx: int = 0
    while idx < len(listy):
        print(listy[idx])
        idx += 1


display(game_points)


# Tests if a value is in the list
list_1: list[int] = [1, 2, 3, 4]
if 4 in list_1:
    print("yay")
