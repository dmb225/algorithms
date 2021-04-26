import pytest


class InvalidSubStrSizeError(Exception):
    pass


def find_substring(s: str, sub: str) -> int:
    """
    :param s: a string
    :param sub: the potential sub str
    :return: the index of sub first item if found else -1
    """
    if len(sub) < 1:
        return 0
    if len(sub) > len(s):
        raise InvalidSubStrSizeError("sub length cannot be bigger than s length")
        return -1
    if len(sub) == len(s):
        return int(sub == s) - 1
    for i in range(len(s)):
        if i + len(sub) <= len(s) and s[i:i + len(sub)] == sub:
            return i
    return -1


@pytest.mark.parametrize('s, sub, res', [
    ('hello', 'll', 2),
    ('aaaaa', 'baa', -1),
    ('a', 'a', 0),
    ('ty', '', 0),
    ('abc', 'c', 2),
])
def test_find_sub_str(s, sub, res):
    assert find_substring(s, sub) == res


@pytest.mark.parametrize('s, sub, res', [
    ('a', 'aa', -1),
    ('', 'a', -1),
])
def test_two_sum_not_enough_items(s, sub, res):
    with pytest.raises(InvalidSubStrSizeError):
        assert find_substring(s, sub) == res
