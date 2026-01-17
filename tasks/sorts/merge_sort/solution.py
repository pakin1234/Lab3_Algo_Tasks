def merge(left_arr: list[int], right_arr: list[int]) -> list[int]:
    """
    Объединяет два отсортированных списка целых чисел в один отсортированный список.

    Args:
        left_arr (list[int]): Первый отсортированный список.
        right_arr (list[int]): Второй отсортированный список.

    Returns:
        list[int]: Новый список, содержащий все элементы из left_arr и right_arr,
                   отсортированные по возрастанию.
    """
    sorted_list = []
    right_arr_index = left_arr_index = 0

    right_arr_len, left_arr_len = len(right_arr), len(left_arr)

    for _ in range(right_arr_len + left_arr_len):
        if left_arr_index < left_arr_len and right_arr_index < right_arr_len:
            if left_arr[left_arr_index] <= right_arr[right_arr_index]:
                sorted_list.append(left_arr[left_arr_index])
                left_arr_index += 1
            else:
                sorted_list.append(right_arr[right_arr_index])
                right_arr_index += 1
        elif left_arr_index == left_arr_len:
            sorted_list.append(right_arr[right_arr_index])
            right_arr_index += 1
        elif right_arr_index == right_arr_len:
            sorted_list.append(left_arr[left_arr_index])
            left_arr_index += 1
    return sorted_list


def merge_sort(arr: list[int]) -> list[int]:
    """
    Сортирует список целых чисел по возрастанию методом слияния (merge sort).

    Args:
        arr (list[int]): Список целых чисел для сортировки.

    Returns:
        list[int]: Новый отсортированный по возрастанию список.
    """
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    return merge(left_arr, right_arr)
