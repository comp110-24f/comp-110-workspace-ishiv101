"""Practicing my conditonals"""


def less_than_10(num: int) -> str:
    """Tell us if num < 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        return "Small Number!"
    else:
        return "Big Number!"
    print("this is the end of the function")


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going of."""
    if alarm is True:
        return "Wake up! Go to Comp 110"
    else:
        return "Keep sleeping. You deserve it. :)"


"""print(less_than_10(num=7))
# print(wake_up(alarm=True))"""


def characters(msg: str) -> None:
    index: int = 0
    while index < len(msg):
        print(msg[index])
        index += 1


characters(msg="bedtime")
