__author__ = "730749614"


def twoSum(nums: list[int], target: int) -> list[int]:
    """prints a list of the two indexes of the numbers from input list that
    add up to target number"""
    idx: int = 0
    sum: int = 0
    count: int = 0
    inty2: int = 0
    first: int = 0
    listy: list[int] = []
    while count < len(nums) - 1:
        first = nums[inty2]
        sum = first
        listy = [inty2]
        if inty2 != idx:
            while idx < len(nums):
                sum += nums[idx]
                listy.append(idx)
                if sum == target:
                    return listy
                else:
                    sum = first
                    idx += 1
                    listy = [inty2]
            else:
                idx = 0
                inty2 += 1
        else:
            idx += 1


print(
    twoSum(
        [
            3,
            4,
            7,
            9,
            5,
            6,
        ],
        11,
    )
)


def twoSum_2(nums: list[int], target: int) -> list[int]:
    """does the same thing but with for loops(for loops)"""
    for num in range(len(nums)):
        for elem in range(len(nums)):
            if (num != elem) and (nums[num] + nums[elem] == target):
                return [num, elem]
            else:
                return []


print(twoSum_2([3, 4, 7, 9], 11))
