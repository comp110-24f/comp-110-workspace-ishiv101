def process_and_reverse_list(listy: list[int]) -> list[int]:
    squared_list: list[int] = []
    for num in listy:
        squared_list.append(num**2)

    sum_list: list[int] = []
    sum: int = 0
    idx: int = 0

    while idx < len(squared_list) - 1:
        sum = squared_list[idx] + squared_list[idx + 1]
        sum_list.append(sum)
        idx += 2

    if len(squared_list) % 2 != 0:
        sum_list.append(squared_list[-1])

    reverse_list: list[int] = []
    idx: int = len(sum_list) - 1
    while idx >= 0:
        reverse_list.append(sum_list[idx])
        idx -= 1

    return reverse_list


print(process_and_reverse_list([7, 8, 9]))
