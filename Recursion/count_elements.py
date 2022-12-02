def count(lst):
    if not lst:
        return 0
    return 1 + count(lst[1:])


if __name__ == "__main__":
    assert count([1, 2, 3, 4, 'knbjbk']) == 5
    assert count([]) == 0
