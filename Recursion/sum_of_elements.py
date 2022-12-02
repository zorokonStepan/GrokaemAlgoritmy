def sum_elements(seq):
    if len(seq) == 0:
        return 0
    return seq[0] + sum_elements(seq[1:])


if __name__ == "__main__":
    assert sum_elements((1, 2, 3, 4, 5)) == 15
