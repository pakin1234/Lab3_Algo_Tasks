def insertion_sort(arr: list[int]) -> list[int]:
    """
    Сортирует список целых чисел по возрастанию методом вставок (insertion sort).

    Args:
        arr (list[int]): Список целых чисел для сортировки.

    Returns:
        list[int]: Отсортированный список (тот же объект, что и на входе).
    """
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
