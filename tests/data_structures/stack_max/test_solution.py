from tasks.data_stuctures.stack_max.solution import StackMax


def test_empty_stack_behavior() -> None:
    """Проверка поведения на пустом стеке."""
    stack = StackMax()

    assert stack.get_max() == "None"
    assert stack.pop() == "error"

    assert stack.get_max() == "None"
    assert stack.pop() == "error"


def test_basic_push_and_max() -> None:
    """Проверка добавления элементов и корректного отслеживания максимума."""
    stack = StackMax()

    stack.push(7)
    assert stack.get_max() == 7

    stack.push(1)
    assert stack.get_max() == 7

    stack.push(10)
    assert stack.get_max() == 10

    stack.push(3)
    assert stack.get_max() == 10


def test_pop_and_max_update() -> None:
    """Проверка обновления максимума после удаления элементов."""
    stack = StackMax()

    stack.push(-2)
    stack.push(-1)
    stack.push(5)
    stack.push(3)

    assert stack.get_max() == 5

    assert stack.pop() is None
    assert stack.get_max() == 5

    assert stack.pop() is None
    assert stack.get_max() == -1

    assert stack.pop() is None
    assert stack.get_max() == -2

    assert stack.pop() is None
    assert stack.get_max() == "None"

    # Попытка pop на пустом стеке
    assert stack.pop() == "error"


def test_example_from_task_1() -> None:
    """Полное воспроизведение первого примера из условия задачи."""
    stack = StackMax()

    assert stack.get_max() == "None"
    stack.push(7)
    assert stack.pop() is None
    stack.push(-2)
    stack.push(-1)
    assert stack.pop() is None
    assert stack.get_max() == -2
    assert stack.get_max() == -2


def test_example_from_task_2() -> None:
    """Полное воспроизведение второго примера из условия задачи."""
    stack = StackMax()

    assert stack.get_max() == "None"
    assert stack.pop() == "error"
    assert stack.pop() == "error"
    assert stack.pop() == "error"
    stack.push(10)
    assert stack.get_max() == 10
    stack.push(-9)


def test_large_sequence() -> None:
    """Проверка корректности при большом количестве операций (O(1) на операцию)."""
    stack = StackMax()
    values = [42, 17, 83, 5, 91, 33, 64, 91, 12, 55]

    current_max = float("-inf")
    for val in values:
        stack.push(val)
        current_max = max(current_max, val)
        assert stack.get_max() == current_max

    for _ in range(5):
        stack.pop()

    remaining_max = max(values[:5])
    assert stack.get_max() == remaining_max

    for _ in range(5):
        assert stack.pop() is None

    assert stack.get_max() == "None"
