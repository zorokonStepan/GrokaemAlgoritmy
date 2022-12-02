def quick_sort(arr):
    """O(n log n)"""
    if len(arr) < 2:  # базовый случай
        return arr
    else:  # рекурсивный случай
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    a = [7, 5, 1, 4, 8, 9, 3, 2, 6]
    assert quick_sort(a) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
