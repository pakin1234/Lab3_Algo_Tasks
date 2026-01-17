def binary_search(arr: list[int], target: int) -> int:
    """
    Выполняет бинарный поиск заданного значения в отсортированном по возрастанию списке целых чисел.

    Args:
        arr (list[int]): Отсортированный по возрастанию список целых чисел.
        target (int): Искомое значение.

    Returns:
        int: Индекс элемента, равного target, если элемент найден; иначе -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
