import pytest
from typing import List


def find_or_insert_pos_v0(nums: List[int], target: int) -> int:
    """
    :param nums: a sorted list of integers
    :param target: the integer we are looking for
    :return: target index if found else the index where it would be inserted
    """
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)


def find_or_insert_pos_v1(nums: List[int], target: int) -> int:
    """
    :param nums: a sorted list of integers
    :param target: the integer we are looking for
    :return: target index if found else the index where it would be inserted
    """
    begin, end = 0, len(nums)
    while begin < end:
        mid = (begin + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            begin = mid + 1
        else:
            end = mid
    return end


@pytest.mark.parametrize('nums, target, res', [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 0, 0),
    ([], 5, 0),
])
def test_find_insert_pos(nums, target, res):
    assert find_or_insert_pos_v0(nums, target) == res
    assert find_or_insert_pos_v1(nums, target) == res
