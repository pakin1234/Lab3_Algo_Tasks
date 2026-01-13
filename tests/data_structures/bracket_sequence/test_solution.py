from tasks.data_stuctures.bracket_sequence.solution import is_correct_bracket_seq


def test_correct_sequences() -> None:
    """Проверка корректных скобочных последовательностей."""
    assert is_correct_bracket_seq("{[()]}") is True
    assert is_correct_bracket_seq("()") is True
    assert is_correct_bracket_seq("") is True
    assert is_correct_bracket_seq("([]){}") is True
    assert is_correct_bracket_seq("((()))[]{}") is True
    assert is_correct_bracket_seq("({[]}((){}))") is True
    assert is_correct_bracket_seq("()[]{}") is True
    assert is_correct_bracket_seq("([{}])") is True


def test_incorrect_sequences() -> None:
    """Проверка некорректных скобочных последовательностей."""
    assert is_correct_bracket_seq("{[(]}") is False
    assert is_correct_bracket_seq("([)") is False
    assert is_correct_bracket_seq(")") is False
    assert is_correct_bracket_seq("(") is False
    assert is_correct_bracket_seq("}{") is False
    assert is_correct_bracket_seq("(((") is False
    assert is_correct_bracket_seq("())") is False
    assert is_correct_bracket_seq("({]}") is False


def test_edge_cases() -> None:
    """Проверка граничных и дополнительных случаев."""
    assert is_correct_bracket_seq("[]") is True
    assert is_correct_bracket_seq("{}") is True
    assert is_correct_bracket_seq("") is True
    assert is_correct_bracket_seq("((({{{[[[()()()]]]}}})))") is True
    assert is_correct_bracket_seq(")({}") is False
