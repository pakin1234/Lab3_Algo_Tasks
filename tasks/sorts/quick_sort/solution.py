import random


def quick_sort(arr: list[int]) -> list[int]:
    """
    Сортирует список целых чисел по возрастанию методом быстрой сортировки (quick sort).

    Args:
        arr (list[int]): Список целых чисел для сортировки.

    Returns:
        list[int]: Новый отсортированный по возрастанию список. Исходный список не модифицируется.
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)
