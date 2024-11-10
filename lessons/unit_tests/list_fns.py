# get_first: takes a list[str] as input and returns the first element"""
def get_first(listy: list[str]) -> str:
    return listy[0]


# remove_first: takes a list[str]  as input and removes the first element
def remove_first(listy: list[str]) -> None:
    listy.pop((0))


# get_and_remove_first: takes a list[str] as input and returns + removes first elem
def get_and_remove_first(listy: list[str]) -> str:
    """remove AND return first element"""
    first_elem: str = listy[0]
    remove_first(listy)  # remove first_elem
    return first_elem


print(get_and_remove_first(["hi", "hello", "welcome"]))
