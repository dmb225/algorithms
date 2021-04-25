import pytest


def reverse_inplace(lst: list) -> None:
    """
    :param lst: a list of characters
    """
    i = 0
    k = len(lst) - 1
    while i < k:
        lst[i], lst[k] = lst[k], lst[i]
        i += 1
        k -= 1


@pytest.mark.parametrize('lst_in, lst_rev', [
    (['h', 'e', 'l', 'l', 'o'], ['o', 'l', 'l', 'e', 'h']),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
])
def test_reverse_alpha_ok(lst_in, lst_rev):
    reverse_inplace(lst_in)
    assert lst_in == lst_rev
