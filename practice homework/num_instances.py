def num_instances(inp_str: str, search_str: str) -> int:
    index: int = 0
    count: int = 0

    while index <= len(inp_str) - len(search_str):
        #the last index possible to search for search_str
        subindex: int = 0

        while subindex <= len(search_str):




print(num_instances(inp_str="HelloHello", search_str="el"))
# should print 2