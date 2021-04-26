import pytest


class EmptyListError(Exception):
    pass


def roman_to_int(s: str) -> int:
    """
    :param s: A roman form number
    :return: The corresponding integer
    """
    if len(s) < 1:
        raise EmptyListError('The roman number should have at least 1 letter')
        return -1
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i, res = 0, 0
    while i < len(s):
        if i < len(s) - 1 and d[s[i]] < d[s[i + 1]]:
            res += d[s[i + 1]] - d[s[i]]
            i += 2
        else:
            res += d[s[i]]
            i += 1
    return res


@pytest.mark.parametrize('roman, res', [
    ('III', 3),
    ('LVIII', 58),
    ('MCMXCIV', 1994),
])
def test_roman_to_int(roman, res):
    assert roman_to_int(roman) == res


@pytest.mark.parametrize('roman, res', [
    ('', -1),
])
def test_two_sum_not_enough_items(roman, res):
    with pytest.raises(EmptyListError):
        assert roman_to_int(roman) == res
