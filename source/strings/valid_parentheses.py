import pytest


def valid_parentheses(s: str) -> bool:
    """
    :param s: a string containing just the characters '(', ')', '{', '}', '[' and ']'
    :return: determine if the input string is valid
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
    """
    if len(s) % 2:
        return False
    d = {'(': ')', '{': '}', '[': ']'}
    stack = list()
    for c in s:
        if c in '({[':
            stack.append(c)
        else:
            if stack:
                if d[stack.pop()] != c:
                    return False
            else:
                return False
    return True


@pytest.mark.parametrize('s, res', [
    ('()', True),
    ('()[]{}', True),
    ('(]', False),
    ('{[]}', True),
])
def test_valid_parentheses(s, res):
    assert valid_parentheses(s) == res
