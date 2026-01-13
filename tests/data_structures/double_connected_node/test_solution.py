from tasks.data_stuctures.double_connected_node.solution import DoubleConnectedNode, solution


def test_reverse_four_elements() -> None:
    """Проверка разворота списка из четырёх элементов (пример из задачи)."""
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1
    node1.prev = node0
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2

    new_head = solution(node0)

    assert new_head is node3
    assert node3.next is node2
    assert node3.prev is None
    assert node2.next is node1
    assert node2.prev is node3
    assert node1.next is node0
    assert node1.prev is node2
    assert node0.next is None
    assert node0.prev is node1


def test_reverse_single_element() -> None:
    """Проверка разворота списка из одного элемента."""
    single = DoubleConnectedNode(100)

    new_head = solution(single)

    assert new_head is single
    assert single.next is None
    assert single.prev is None


def test_reverse_two_elements() -> None:
    """Проверка разворота списка из двух элементов."""
    node_a = DoubleConnectedNode("A")
    node_b = DoubleConnectedNode("B")

    node_a.next = node_b
    node_b.prev = node_a

    new_head = solution(node_a)

    assert new_head is node_b
    assert node_b.next is node_a
    assert node_b.prev is None
    assert node_a.next is None
    assert node_a.prev is node_b


def test_reverse_three_elements() -> None:
    """Проверка разворота списка из трёх элементов."""
    n1 = DoubleConnectedNode(1)
    n2 = DoubleConnectedNode(2)
    n3 = DoubleConnectedNode(3)

    n1.next = n2
    n2.prev = n1
    n2.next = n3
    n3.prev = n2

    new_head = solution(n1)

    assert new_head is n3
    assert n3.next is n2 and n3.prev is None
    assert n2.next is n1 and n2.prev is n3
    assert n1.next is None and n1.prev is n2


def test_reverse_long_list() -> None:
    """Проверка разворота длинного списка (линейная сложность O(n))."""
    nodes = [DoubleConnectedNode(i) for i in range(10)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]

    new_head = solution(nodes[0])

    assert new_head is nodes[-1]

    # Проверка прямого порядка (9 → 8 → ... → 0)
    current_forward: DoubleConnectedNode | None = new_head
    for i in range(9, -1, -1):
        assert current_forward is not None
        assert current_forward.value == i
        current_forward = current_forward.next

    # Проверка обратных ссылок (0 ← 1 ← ... ← 9)
    current_backward: DoubleConnectedNode | None = nodes[0]
    for i in range(0, 10):
        assert current_backward is not None
        assert current_backward.value == i
        current_backward = current_backward.prev if current_backward.prev else None
