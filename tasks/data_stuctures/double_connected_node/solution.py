class DoubleConnectedNode:
    def __init__(
        self,
        value: str | int,
        next: "DoubleConnectedNode | None" = None,
        prev: "DoubleConnectedNode | None" = None,
    ) -> None:
        self.value = value
        self.next = next
        self.prev = prev


def solution(node: DoubleConnectedNode | None) -> DoubleConnectedNode | None:
    """
    Разворачивает двусвязный список, меняя порядок элементов на обратный.

    Args:
        node (DoubleConnectedNode): Голова исходного списка (первый узел).

    Returns:
        DoubleConnectedNode: Голова развёрнутого списка (бывший последний узел).
    """
    current_node = node
    new_head = None

    while current_node is not None:
        next_node = current_node.next
        current_node.next = current_node.prev
        current_node.prev = next_node
        new_head = current_node
        current_node = next_node

    return new_head
