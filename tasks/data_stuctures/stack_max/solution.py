class StackMax:
    def __init__(self) -> None:
        """
        Инициализирует пустой стек с поддержкой быстрого получения максимума.
        """
        self.items: list[int] = []
        self.max_stack: list[int] = []

    def push(self, x: int) -> None:
        """
        Добавляет элемент x на вершину стека.

        Args:
            x (int): Добавляемое целое число.
        """
        self.items.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self) -> str | None:
        """
        Удаляет элемент с вершины стека.

        Returns:
            str | None: "error", если стек пуст; иначе None.
        """
        if not self.items:
            return "error"

        removed = self.items.pop()
        if removed == self.max_stack[-1]:
            self.max_stack.pop()

        return None

    def get_max(self) -> int | str | None:
        """
        Возвращает максимальный элемент в стеке.

        Returns:
            int | str | None: Максимальное значение, "None" при пустом стеке.
        """
        if not self.items:
            return "None"

        return self.max_stack[-1]
