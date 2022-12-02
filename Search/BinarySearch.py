from typing import Union


def binary_search(lst: Union[list, tuple], search_element):
    """O(log n)"""
    # low - нижняя, high - верхняя границы поиска
    low = 0
    high = len(lst) - 1

    while low <= high:  # Пока эта часть не сократится до одного эnемента
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == search_element:
            return mid
        if guess > search_element:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    my_list = (1, 3, 5, 7, 9)

    assert binary_search(my_list, 3) == 1
    assert binary_search(my_list, 9) == 4
    assert binary_search(my_list, 7) == 3
