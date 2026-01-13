from collections.abc import Sequence

from tasks.data_stuctures.update_list.solution import Node, solution


def build_list(values: Sequence[int | str]) -> Node | None:
    """Вспомогательная функция для создания списка из значений."""
    head = None
    for val in reversed(values):
        head = Node(val, head)
    return head


def list_to_values(head: Node | None) -> list:
    """Вспомогательная функция для преобразования списка в список значений."""
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next_item
    return values


def test_remove_first_element() -> None:
    """Проверка удаления первого элемента (idx = 0)."""
    head = build_list(["node0", "node1", "node2", "node3"])
    assert head is not None
    new_head = solution(head, 0)

    assert new_head == head.next_item
    assert new_head is not None
    assert list_to_values(new_head) == ["node1", "node2", "node3"]


def test_remove_middle_element() -> None:
    """Проверка удаления элемента из середины списка (пример из задачи)."""
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)

    new_head = solution(node0, 1)

    assert new_head is node0
    assert list_to_values(new_head) == ["node0", "node2", "node3"]
    assert new_head.next_item is node2
    assert node2.next_item is node3
    assert node3.next_item is None


def test_remove_last_element() -> None:
    """Проверка удаления последнего элемента."""
    head = build_list([1, 2, 3, 4, 5])
    new_head = solution(head, 4)

    assert new_head is head
    assert list_to_values(new_head) == [1, 2, 3, 4]
    current: Node | None = new_head
    while current is not None and current.next_item is not None:
        current = current.next_item
    assert current is not None
    assert current.value == 4
    assert current.next_item is None


def test_remove_only_element() -> None:
    """Проверка удаления единственного элемента (список становится пустым)."""
    single = Node("only")
    new_head = solution(single, 0)

    assert new_head is None


def test_remove_in_long_list() -> None:
    """Проверка удаления в длинном списке (линейная сложность O(n))."""
    values = list(range(100))
    head = build_list(values)

    new_head = solution(head, 50)

    expected = values[:50] + values[51:]
    assert list_to_values(new_head) == expected
    assert new_head is head


def test_remove_near_end() -> None:
    """Проверка удаления элемента близко к концу списка."""
    head = build_list(["a", "b", "c", "d", "e"])
    new_head = solution(head, 3)

    assert list_to_values(new_head) == ["a", "b", "c", "e"]
    assert new_head is head
