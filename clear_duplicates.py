import pytest


def clear_duplicates(lst: list) -> list:
    return list(dict.fromkeys(lst))


@pytest.mark.parametrize('lst, res', [
    ([1, 1, 1], [1]),
    ([1, 2, 1], [1, 2]),
    ([3, 2, 1, 1, 2, 3], [3, 2, 1]),
])
def test_clear_duplicates_removes_duplicate_elements(lst, res):
    assert clear_duplicates(lst) == res
