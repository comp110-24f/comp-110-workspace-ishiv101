stats: list[int] = [7, 8, 9]
index: int = 0
total: int = 100
while index < len(stats):
    total -= stats[index]
    index += 1
print(total)

stats: list[int] = [7, 8, 9]
total: int = 100
for num in stats:
    total -= num
print(total)

stats: list[int] = [7, 8, 9]
total: int = 100
for idx in range(0, len(stats)):
    total -= stats[idx]
print(total)


listy: list[int] = [1, 2, 3, 4]


# strings are iterable
stringy: str = "1234"
for digit in stringy:
    print(digit)

# can use += operator for strings
stringy += "5"
print(stringy)

# integers are not iterable

inty: int = 1234
for digit in inty:
    print(digit)

# can use += operator for integers
inty += 1
print(inty)
