import pytest
from unittest.mock import sentinel


def clear_duplicates(lst: list) -> list:
    """
        Remove duplicate items in a given list
        @input: a list
        @output: a list with unique word
        Ex:
            - clear_duplicates([1, 1, 1]) = [1]
            - clear_duplicates([1, 2, 1]) = [1, 2]
    """
    return list(dict.fromkeys(lst))


@pytest.mark.parametrize('lst, res', [
    ([1, 1, 1], [1]),
    ([1, 2, 1], [1, 2]),
    ([3, 2, 1, 1, 2, 3], [3, 2, 1]),
])
def test_clear_duplicates_removes_duplicate_elements(lst, res):
    assert clear_duplicates(lst) == res


def test_clear_duplicates_does_not_affect_lists_without_duplicates():
    lst = [sentinel.el1, sentinel.el2, sentinel.el3]
    assert clear_duplicates(lst) == lst
