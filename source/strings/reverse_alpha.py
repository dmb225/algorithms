import pytest


def reverse_alpha(str_in: str) -> str:
    """
    :param str_in: a str
    :return: a str where str_in alpha characters are reversed
    """
    lst = [c for c in str_in]
    i = 0
    k = len(lst) - 1
    while i < k:
        if not lst[i].isalpha():
            i += 1
            continue
        if not lst[k].isalpha():
            k -= 1
            continue
        lst[i], lst[k] = lst[k], lst[i]
        i += 1
        k -= 1
    return ''.join(lst)


@pytest.mark.parametrize('str_in, str_rev', [
    ("a!!!b.c.d,e'f,ghi", "i!!!h.g.f,e'd,cba"),
])
def test_reverse_alpha_ok(str_in, str_rev):
    assert reverse_alpha(str_in) == str_rev


@pytest.mark.parametrize('str_in, str_rev', [
    ("a!!!b.c.d,e'f,ghi", "ihg,f'e,d.c.b!!!a"),
])
def test_reverse_alpha_ko(str_in, str_rev):
    assert not reverse_alpha(str_in) == str_rev
