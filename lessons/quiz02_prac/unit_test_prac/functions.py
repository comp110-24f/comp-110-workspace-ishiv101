def find_even(nums: list[int]) -> int:
    """returns the first even number in input list"""
    idx: int = 0
    while idx < len(nums):
        if nums[idx] % 2 == 0:
            return idx
        idx += 1
    return -1


def add_key_to_dicts(dicts: list[dict], key: str, value: int) -> None:
    """adds new key-value pairs to each dict in list of dicts"""
    for d in dicts:
        d[key] = value
