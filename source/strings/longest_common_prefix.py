import pytest
from typing import List


def common_prefix(s1: str, s2: str) -> str:
    """
    :param s1: a string
    :param s2: a string
    :return: the common prefix of s1 and s2
    """
    cp = ''
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            return cp
        cp += c1
    return cp


def longest_common_prefix(strings: List[str]) -> str:
    """
    :param strings: a list of strings
    :return: the longest common prefix of these strings
    """
    lcp = strings[0]
    for i in range(1, len(strings)):
        cp = common_prefix(strings[i - 1], strings[i])
        lcp = min(lcp, cp)
    return lcp


@pytest.mark.parametrize('strings, res', [
    (['flower', 'flow', 'flight'], 'fl'),
    (['dog', 'racecar', 'car'], ''),
])
def test_longest_common_prefix(strings, res):
    assert longest_common_prefix(strings) == res
