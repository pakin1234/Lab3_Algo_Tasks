from tasks.sorts.insertion_sort.solution import insertion_sort


def test_empty_list() -> None:
    """Проверка сортировки пустого списка."""
    arr: list[int] = []
    result = insertion_sort(arr)

    assert result == []
    assert result is arr


def test_single_element() -> None:
    """Проверка списка из одного элемента."""
    arr: list[int] = [42]
    result = insertion_sort(arr)

    assert result == [42]
    assert result is arr


def test_example_from_task() -> None:
    """Проверка на примере из условия задачи."""
    arr: list[int] = [9, 5, 1, 4, 3]
    result = insertion_sort(arr)

    assert result == [1, 3, 4, 5, 9]
    assert result is arr
    assert arr == [1, 3, 4, 5, 9]


def test_reverse_sorted() -> None:
    """Проверка полностью обратного массива."""
    arr: list[int] = [5, 4, 3, 2, 1]
    result = insertion_sort(arr)

    assert result == [1, 2, 3, 4, 5]
    assert result is arr
    assert arr == [1, 2, 3, 4, 5]


def test_with_duplicates_and_negatives() -> None:
    """Проверка массива с дубликатами и отрицательными числами."""
    arr: list[int] = [2, -1, 2, -1, 0]
    result = insertion_sort(arr)

    assert result == [-1, -1, 0, 2, 2]
    assert result is arr
    assert arr == [-1, -1, 0, 2, 2]


def test_already_sorted() -> None:
    """Проверка уже отсортированного массива."""
    arr: list[int] = [-5, -3, 0, 1, 2, 7]
    result = insertion_sort(arr)

    assert result == [-5, -3, 0, 1, 2, 7]
    assert result is arr
    assert arr == [-5, -3, 0, 1, 2, 7]


def test_large_random_array() -> None:
    """Проверка на массиве максимальной длины (подтверждение O(n²) устойчивости)."""
    import random

    values = list(range(-500, 500))
    random.shuffle(values)
    arr: list[int] = values[:1000]

    result = insertion_sort(arr)

    expected = sorted(values[:1000])
    assert result == expected
    assert result is arr
    assert all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
