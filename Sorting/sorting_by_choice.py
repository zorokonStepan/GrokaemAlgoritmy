"""O(n ** 2)"""

def find_smallest(arr):
    """возвращает индекс наименьшего элемента последовательности"""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list):
    """
    при каждом обходе списка находит минимальное значение,
    удаляет это значение из изначального списка и добовляет в
    новый список, который возвращается в результате работы функции
    """
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


if __name__ == "__main__":
    assert selection_sort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
