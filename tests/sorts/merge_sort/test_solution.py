from tasks.sorts.merge_sort.solution import merge_sort


def test_empty_array() -> None:
    """Проверка сортировки пустого массива."""
    arr: list[int] = []
    result = merge_sort(arr)

    assert result == []
    assert arr == []


def test_single_element() -> None:
    """Проверка массива из одного элемента."""
    arr: list[int] = [42]
    result = merge_sort(arr)

    assert result == [42]
    assert arr == [42]


def test_already_sorted() -> None:
    """Проверка уже отсортированного массива."""
    arr: list[int] = [-5, -1, 0, 3, 7, 10]
    result = merge_sort(arr)

    assert result == [-5, -1, 0, 3, 7, 10]
    assert arr == [-5, -1, 0, 3, 7, 10]


def test_reverse_sorted() -> None:
    """Проверка массива, отсортированного в обратном порядке."""
    arr: list[int] = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    result = merge_sort(arr)

    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert arr == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def test_with_duplicates_and_negatives() -> None:
    """Проверка массива с повторяющимися значениями и отрицательными числами."""
    arr: list[int] = [2, -1, 2, -1, 0, -5, 5, 2, -3]
    result = merge_sort(arr)

    assert result == [-5, -3, -1, -1, 0, 2, 2, 2, 5]
    assert arr == [2, -1, 2, -1, 0, -5, 5, 2, -3]


def test_example_from_task() -> None:
    """Проверка на примере из условия задачи."""
    arr: list[int] = [4, 5, 3, 0, 1, 2]
    result = merge_sort(arr)

    assert result == [0, 1, 2, 3, 4, 5]
    assert arr == [4, 5, 3, 0, 1, 2]


def test_large_array() -> None:
    """Проверка на массиве максимальной длины (подтверждение O(n log n) и устойчивости)."""
    import random

    values = list(range(-50000, 50000))
    random.shuffle(values)
    arr: list[int] = values[:100000]  # n = 10^5

    result = merge_sort(arr)

    expected = sorted(values[:100000])
    assert result == expected
    assert arr != expected
    assert all(result[i] <= result[i + 1] for i in range(len(result) - 1))
