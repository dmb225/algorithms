import pytest


def longest_substring_length(s: str) -> int:
    """
    :param s: a string
    :return: the length of the longest substring with no duplicates
    """
    d = {}
    res, start = 0, -1
    for i, c in enumerate(s):
        if c in d and d[c] > start:
            start = d[c]
        res = max(res, i - start)
        d[c] = i
    return res


@pytest.mark.parametrize('s, res', [
    ('abcabcbb', 3),
    ('bbbbbb', 1),
    ('pwwkew', 3),
    ('', 0),
])
def test_longest_substring_length(s, res):
    assert longest_substring_length(s) == res
