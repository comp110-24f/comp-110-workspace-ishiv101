for x in "string":
    print(x)

pet: list[str] = ["Louie", "Bo", "Bear"]
for item in pet:
    print(f"Good Boy, {item}!")

for item in ["hi", 4, "hello"]:
    print(item)
    print(type(item))

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
# print each index: name
for index in range(0, len(names)):
    print(f"{index}: {names[index]}")
