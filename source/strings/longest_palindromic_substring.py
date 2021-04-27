import pytest


def get_palindrome(s: str, b: int, e: int) -> str:
    while b >= 0 and e < len(s) and s[b] == s[e]:
        b -= 1
        e += 1
    return s[b + 1:e]  # r is already an outer index


def longest_palindromic_substring(s: str) -> str:
    """
    :param s: a string
    :return: the longest palindromic substring in s
    """
    p = ''
    for i in range(len(s)):
        p1 = get_palindrome(s, i, i + 1)  # even length
        p2 = get_palindrome(s, i, i)  # odd length
        p = max([p, p1, p2], key=lambda x: len(x))
    return p


@pytest.mark.parametrize('s, res', [
    ('babad', 'bab'),
    ('cbbd', 'bb'),
    ('a', 'a'),
    ('ac', 'a'),
])
def test_longest_palindromic_substring(s, res):
    assert longest_palindromic_substring(s) == res
