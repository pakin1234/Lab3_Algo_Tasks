def is_correct_bracket_seq(s: str) -> bool:
    """
    Проверяет, является ли строка корректной скобочной последовательностью.

    Args:
        s (str): Строка, состоящая только из скобок '()[]{}'.

    Returns:
        bool: True, если скобки расставлены корректно; иначе False.
    """
    stack = []
    opening_brackets = ("(", "{", "[")
    closing_brackets = (")", "}", "]")
    for character in s:
        if character in opening_brackets:
            stack.append(opening_brackets.index(character))
        elif character in closing_brackets:
            if stack and stack[-1] == closing_brackets.index(character):
                stack.pop()
            else:
                return False
    return not stack
