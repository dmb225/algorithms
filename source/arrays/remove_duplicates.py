import pytest
from typing import List
from unittest.mock import sentinel


def remove_duplicates(lst: list) -> list:
    """
    :param lst: a list
    :return: a list with unique word
    """
    return list(dict.fromkeys(lst))


def remove_duplicates_from_sorted_inplace(nums: List[int]) -> int:
    """
    :param nums: a list of integers
    :return: the list without duplicated items
    """
    if len(nums) < 1:
        return 0
    n = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[n] = nums[i]
            n += 1
    return n


@pytest.mark.parametrize('lst, res', [
    ([1, 1, 1], [1]),
    ([1, 2, 1], [1, 2]),
    ([3, 2, 1, 1, 2, 3], [3, 2, 1]),
])
def test_clear_duplicates_removes_duplicate_elements(lst, res):
    assert remove_duplicates(lst) == res


def test_clear_duplicates_does_not_affect_lists_without_duplicates():
    lst = [sentinel.el1, sentinel.el2, sentinel.el3]
    assert remove_duplicates(lst) == lst


@pytest.mark.parametrize('nums, res', [
    ([1, 1, 2], 2),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
    ([1], 1),
    ([], 0),
])
def test_remove_duplicates_from_sorted_inplace(nums, res):
    assert remove_duplicates_from_sorted_inplace(nums) == res
    assert nums[:res] == remove_duplicates(nums)
