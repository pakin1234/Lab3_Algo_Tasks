from tasks.recursion.binary_search.solution import binary_search


def test_found_in_middle() -> None:
    """Проверка поиска элемента в середине массива."""
    arr: list[int] = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3


def test_found_first_element() -> None:
    """Проверка поиска первого элемента."""
    arr: list[int] = [2, 4, 6, 8, 10]
    assert binary_search(arr, 2) == 0


def test_found_last_element() -> None:
    """Проверка поиска последнего элемента."""
    arr: list[int] = [1, 2, 3, 4, 5]
    assert binary_search(arr, 5) == 4


def test_not_found() -> None:
    """Проверка случая, когда элемент отсутствует."""
    arr: list[int] = [1, 3, 5, 7, 9]
    assert binary_search(arr, 4) == -1
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 10) == -1


def test_duplicates() -> None:
    """Проверка поиска в массиве с дубликатами (возвращается любой валидный индекс)."""
    arr: list[int] = [1, 2, 2, 2, 3, 4, 5]
    index = binary_search(arr, 2)
    assert index in (1, 2, 3)
    assert arr[index] == 2


def test_empty_array() -> None:
    """Проверка поиска в пустом массиве."""
    arr: list[int] = []
    assert binary_search(arr, 42) == -1


def test_single_element_found() -> None:
    """Проверка массива из одного элемента — найден."""
    arr: list[int] = [100]
    assert binary_search(arr, 100) == 0


def test_single_element_not_found() -> None:
    """Проверка массива из одного элемента — не найден."""
    arr: list[int] = [100]
    assert binary_search(arr, 99) == -1


def test_large_array() -> None:
    """Проверка на большом массиве (подтверждение O(log n) сложности)."""
    arr: list[int] = list(range(0, 1000000, 2))
    assert binary_search(arr, 500000) == 250000
    assert binary_search(arr, 999998) == 499999
    assert binary_search(arr, 1) == -1
    assert binary_search(arr, -10) == -1
    assert binary_search(arr, 1000000) == -1
