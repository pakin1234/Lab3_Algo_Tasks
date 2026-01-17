from tasks.sorts.bubble_sort.solution import bubble_sort


def test_already_sorted() -> None:
    """Проверка случая, когда массив изначально отсортирован — должен быть один снимок."""
    arr = [1, 2, 3, 4, 5]
    result = bubble_sort(arr)

    assert result == [[1, 2, 3, 4, 5]]
    assert arr == [1, 2, 3, 4, 5]


def test_reverse_sorted() -> None:
    """Проверка полностью обратного массива."""
    arr = [5, 4, 3, 2, 1]
    result = bubble_sort(arr)

    expected = [[4, 3, 2, 1, 5], [3, 2, 1, 4, 5], [2, 1, 3, 4, 5], [1, 2, 3, 4, 5]]
    assert result == expected
    assert arr == [1, 2, 3, 4, 5]


def test_with_duplicates() -> None:
    """Проверка массива с повторяющимися элементами."""
    arr = [3, 1, 4, 1, 5, 9, 2]
    result = bubble_sort(arr)

    expected = [
        [1, 3, 1, 4, 5, 2, 9],
        [1, 1, 3, 4, 2, 5, 9],
        [1, 1, 3, 2, 4, 5, 9],
        [1, 1, 2, 3, 4, 5, 9],
    ]
    assert result == expected
    assert arr == [1, 1, 2, 3, 4, 5, 9]


def test_example_from_task() -> None:
    """Проверка на примере из условия задачи."""
    arr = [3, 7, 9, 4, 3, 1, 8, 5]
    result = bubble_sort(arr)

    expected = [
        [3, 7, 4, 3, 1, 8, 5, 9],
        [3, 4, 3, 1, 7, 5, 8, 9],
        [3, 3, 1, 4, 5, 7, 8, 9],
        [3, 1, 3, 4, 5, 7, 8, 9],
        [1, 3, 3, 4, 5, 7, 8, 9],
    ]
    assert result == expected
    assert arr == [1, 3, 3, 4, 5, 7, 8, 9]


def test_almost_sorted() -> None:
    """Проверка почти отсортированного массива — должна быть ранняя остановка."""
    arr = [1, 2, 4, 3, 5, 6, 7]
    result = bubble_sort(arr)

    expected = [[1, 2, 3, 4, 5, 6, 7]]
    assert result == expected
    assert arr == [1, 2, 3, 4, 5, 6, 7]
