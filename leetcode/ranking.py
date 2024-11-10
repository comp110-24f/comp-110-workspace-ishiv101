__author__ = "730749614"


def ranking(arr: list[int]) -> list[int]:
    count: int = 0
    rank: list[int] = [0] * len(arr)
    # for each element in arr
    for num in range(len(arr)):
        count = 1  # rank starts at 1
        # compare with every other element
        for digi in range(len(arr)):
            if arr[num] > arr[digi]:
                count += 1
        rank[num] = count

    unique_ranks = []
    adjusted_ranks = [0] * len(arr)
    for i in range(len(arr)):
        if rank[i] not in unique_ranks:
            unique_ranks.append(rank[i])
        adjusted_ranks[i] = unique_ranks.index(rank[i]) + 1

    return adjusted_ranks


# not giving correct output
print(ranking([37, 12, 28, 9, 100, 56, 80, 5, 12]))
