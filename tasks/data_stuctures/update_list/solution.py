class Node:
    def __init__(self, value: str | int | float, next_item: "Node | None" = None) -> None:
        self.value = value
        self.next_item = next_item


def solution(node: Node | None, idx: int) -> Node | None:
    """
    Удаляет элемент односвязного списка по заданному индексу (нумерация с нуля)
    и возвращает голову обновлённого списка.

    Args:
        node (Node): Голова исходного списка.
        idx (int): Индекс удаляемого элемента (0 ≤ idx < длина списка).

    Returns:
        Node: Голова списка после удаления элемента (или None, если список стал пустым).
    """
    if idx == 0:
        return node.next_item if node else None

    current = node
    pos = 0
    while current and pos < idx - 1:
        current = current.next_item
        pos += 1
    if current and current.next_item:
        current.next_item = current.next_item.next_item
    return node
