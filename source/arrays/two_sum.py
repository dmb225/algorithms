import pytest
from typing import Tuple


class NotEnoughItemsError(Exception):
    pass


def two_sum(nums: Tuple[int], target: int) -> Tuple[int]:
    """
    :param nums: a tuple of integers
    :param target: a integer which is to the sum of 2 items in nums
    :return: The indexes of the 2 preceding items
    """
    if len(nums) < 2:
        raise NotEnoughItemsError('The tuple should have at least 2 items')
        return -1, -1
    d = dict()
    for i in range(len(nums)):
        if (target - nums[i]) in d:
            return d[target - nums[i]], i
        d[nums[i]] = i
    return 0, 1


@pytest.mark.parametrize('nums, target, res', [
    ((2, 7, 11, 15), 9, (0, 1)),
    ((3, 2, 4), 6, (1, 2)),
    ((3, 3), 6, (0, 1)),
])
def test_two_sum(nums, target, res):
    assert two_sum(nums, target) == res


@pytest.mark.parametrize('nums, target, res', [
    ((1,), 1, (-1, -1)),
    ((), 0, (-1, -1)),
])
def test_two_sum_not_enough_items(nums, target, res):
    with pytest.raises(NotEnoughItemsError):
        assert two_sum(nums, target) == res
