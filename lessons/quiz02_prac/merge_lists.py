def merge_lists(words: list[str], vals: list[int]) -> dict[str, int]:
    # If the lists are not same size return empty dict
    if len(words) != len(vals):
        return {}
    idx: int = 0
    merged: dict[str, int] = {}
    while idx < len(words):
        # at key words[idx] store the number at vals[idx]
        merged[words[idx]] = vals[idx]
        idx += 1
    return merged
