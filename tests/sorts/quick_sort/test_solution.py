import random

from tasks.sorts.quick_sort.solution import quick_sort


def test_empty_array() -> None:
    """Проверка сортировки пустого массива."""
    arr: list[int] = []
    result = quick_sort(arr)

    assert result == []
    assert arr == []


def test_single_element() -> None:
    """Проверка массива из одного элемента."""
    arr: list[int] = [42]
    result = quick_sort(arr)

    assert result == [42]
    assert arr == [42]


def test_example_from_task() -> None:
    """Проверка на примере из условия задачи."""
    arr: list[int] = [3, 7, 9, 4, 3, 1, 8, 5]
    result = quick_sort(arr)

    assert result == [1, 3, 3, 4, 5, 7, 8, 9]
    assert arr == [3, 7, 9, 4, 3, 1, 8, 5]


def test_reverse_sorted() -> None:
    """Проверка массива в обратном порядке."""
    arr: list[int] = [5, 4, 3, 2, 1]
    result = quick_sort(arr)

    assert result == [1, 2, 3, 4, 5]
    assert arr == [5, 4, 3, 2, 1]


def test_with_duplicates_and_negatives() -> None:
    """Проверка массива с дубликатами и отрицательными числами."""
    arr: list[int] = [2, -1, 2, -1, 0]
    result = quick_sort(arr)

    assert result == [-1, -1, 0, 2, 2]
    assert arr == [2, -1, 2, -1, 0]


def test_already_sorted() -> None:
    """Проверка уже отсортированного массива."""
    arr: list[int] = [-10, -5, 0, 1, 3, 7, 10]
    result = quick_sort(arr)

    assert result == [-10, -5, 0, 1, 3, 7, 10]
    assert arr == [-10, -5, 0, 1, 3, 7, 10]


def test_large_random_array() -> None:
    """Проверка на массиве максимальной длины (подтверждение средней O(n log n) сложности)."""
    random.seed(42)
    values = list(range(-50000, 50000))
    random.shuffle(values)
    arr: list[int] = values[:100000]

    result = quick_sort(arr)

    expected = sorted(values[:100000])
    assert result == expected
    assert arr != expected
    assert all(result[i] <= result[i + 1] for i in range(len(result) - 1))
