"""Examples of dictionary syntex with Ice Cream Shop order tallies"""

ice_cream: dict[str, int] = {
    "choclate": 12,
    "vanilla": 8,
    "strawberry": 4,
    # comma after last entry is useful for when you want to add a new entry
}

print(ice_cream["choclate"])


#  len evaluates to number of key-value entries
print(len(ice_cream))

# in key word
print("caramel" in ice_cream)  # False
print("vanilla" in ice_cream)  # True
# case sensitive
print("Vanilla" in ice_cream)  # False

# add key-value entries using subscription notation
ice_cream["mint"] = 10
ice_cream["mint"] += 10
print(ice_cream)

# access values by their key using subscription notation
mint_orders: int = ice_cream["mint"]
print(mint_orders)

# Re-assign values by their key using assingment operator
ice_cream["mint"] = ice_cream["mint"] + 1
ice_cream["mint"] += 1

# Remove items by key using the pop method
print(ice_cream.pop("strawberry"))

# Test if a key is in the dictionary:
# not the same for lists
print("strawberry" in ice_cream)
print("vanilla" in ice_cream)

# Loop though items using for-in loops
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print({f"{flavor}: {tally}"})

# print keys
for flavor in ice_cream:
    print(flavor)
