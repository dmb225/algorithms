import pytest
from typing import List
from itertools import accumulate


def maximum_sub_sum(nums: List[int]) -> int:
    """
    :param nums: a list of integer
    :return: the sum of nums's subarray which has the largest sum
    """
    return max(accumulate(nums, lambda x, y: y if y > x + y else x + y))


@pytest.mark.parametrize('nums, res', [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
])
def test_maximum_sub_sum(nums, res):
    assert maximum_sub_sum(nums) == res
