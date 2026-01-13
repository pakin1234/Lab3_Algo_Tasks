from contextlib import redirect_stdout
from io import StringIO
from typing import Any

from tasks.data_stuctures.tasks_list.solution import Node, solution


def capture_output(func: Any, *args: Any) -> list[str]:
    """Вспомогательная функция для захвата вывода print."""
    output = StringIO()
    with redirect_stdout(output):
        func(*args)
    return output.getvalue().strip().split("\n")


def test_print_single_element() -> None:
    """Проверка печати списка из одного элемента."""
    node = Node("single")

    printed_lines = capture_output(solution, node)

    assert printed_lines == ["single"]


def test_print_four_elements() -> None:
    """Проверка печати списка из четырёх элементов (пример из задачи)."""
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)

    printed_lines = capture_output(solution, node0)

    assert printed_lines == ["node0", "node1", "node2", "node3"]


def test_print_three_elements() -> None:
    """Проверка печати списка из трёх элементов."""
    n1 = Node(1)
    n2 = Node(2, n1)
    n3 = Node(3, n2)

    printed_lines = capture_output(solution, n3)

    assert printed_lines == ["3", "2", "1"]


def test_print_with_different_types() -> None:
    """Проверка печати списка с элементами разных типов (строки, числа)."""
    node3 = Node(100)
    node2 = Node("middle")
    node1 = Node(True, node2)
    node0 = Node(42.5, node1)
    node2.next_item = node3

    printed_lines = capture_output(solution, node0)

    assert printed_lines == ["42.5", "True", "middle", "100"]


def test_print_long_list() -> None:
    """Проверка печати длинного списка (линейная сложность O(n))."""
    head = None
    for i in reversed(range(100)):
        head = Node(i, head)

    printed_lines = capture_output(solution, head)

    expected = [str(i) for i in range(100)]
    assert printed_lines == expected


def test_minimum_length_list() -> None:
    """Проверка минимального списка (хотя по ограничениям ≥1 элемент)."""
    node = Node("only_one")

    printed_lines = capture_output(solution, node)

    assert printed_lines == ["only_one"]
    assert len(printed_lines) == 1
