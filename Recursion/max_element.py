def max_element(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max_element(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


if __name__ == "__main__":
    assert max_element([2, 44, 3, 6, 7]) == 44
