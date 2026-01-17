class Node:
    def __init__(self, value: str | int | float, next_item: "Node | None" = None) -> None:
        self.value = value
        self.next_item = next_item


def solution(node: Node | None) -> None:
    """
    Печатает значения всех элементов односвязного списка по порядку от головы до конца.

    Args:
        node (Node): Голова односвязного списка (первый узел).

    Returns:
        None
    """
    while node:
        print(node.value)
        node = node.next_item
