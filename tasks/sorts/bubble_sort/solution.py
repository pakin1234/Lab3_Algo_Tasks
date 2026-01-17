def bubble_sort(arr: list[int]) -> list[list[int]]:
    """
    Возвращает список снимков состояния массива в процессе пузырьковой сортировки.

    Args:
        arr (list[int]): Список целых чисел, который будет сортирован in-place.

    Returns:
        list[list[int]]: Список копий массива после каждого прохода, в котором произошёл
                         хотя бы один обмен.
                         Если обменов не было ни в одном проходе (массив уже отсортирован),
                         возвращается список с одним элементом — копией исходного массива.
    """
    snapshots = []
    n = len(arr)
    swapped_in_any_pass = False

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                swapped_in_any_pass = True
        if swapped:
            snapshots.append(arr[:])
        else:
            break
    if not swapped_in_any_pass:
        snapshots.append(arr[:])

    return snapshots
