import pytest
import re


def reverse_words(s: str) -> str:
    """
    :param s: a string of separated words
    :return: a string with the same words in reversed order
    """
    lst = re.findall('[a-z0-9]+', s, flags=re.IGNORECASE)
    return ' '.join(lst[::-1])


@pytest.mark.parametrize('s, res', [
    ('the sky is blue', 'blue is sky the'),
    ('  hello world  ', 'world hello'),
    ('  Bob    Loves  Alice   ', 'Alice Loves Bob')
])
def test_reverse_words(s, res):
    assert reverse_words(s) == res
