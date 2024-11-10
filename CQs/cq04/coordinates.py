__author__ = "730749614"


def get_coords(xs: str, ys: str) -> None:
    idx1: int = 0
    idx2: int = 0
    while idx1 < len(xs):
        idx2 = 0
        while idx2 < len(ys):
            print(f"({xs[idx1]},{ys[idx2]})")
            idx2 += 1
        idx1 += 1

