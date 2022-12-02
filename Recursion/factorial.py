from math import prod


def fact(x):
    if x == 1:
        return 1
    return x * fact(x - 1)


if __name__ == "__main__":
    assert fact(5) == prod(range(1, 6))
    assert fact(100) == prod(range(1, 101))
