import pytest
from typing import List


class EmptyListError(Exception):
    pass


def remove_item_inplace(nums: List[int], val: int) -> int:
    """
    :param nums: a list of integer
    :param val: the value we want to remove from the list
    :return: the length of the list after remove all val occurrences
    """
    if val not in nums:
        return len(nums)
    n = 0
    for item in nums:
        if item != val:
            nums[n] = item
            n += 1
    return n


@pytest.mark.parametrize('nums, val, res', [
    ([3, 2, 2, 3], 3, 2),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
    ([3, 2, 2, 3], 1, 4),
    ([], 1, 0),
])
def remove_item_inplace(nums, val, res):
    assert remove_item_inplace(nums, val) == res
    assert nums[:res] == [nums[i] for i in range(res) if nums[i] != val]
