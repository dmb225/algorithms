import pytest
from typing import List, Tuple


def three_sum(nums: List[int]) -> List[Tuple[int]]:
    """
    :param nums: a list of integers
    :return:  all the triplets [nums[i], nums[j], nums[k]] such that
              i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0
    """
    nums.sort()
    r = list()
    for k in range(len(nums)):
        target = -nums[k]
        i, j = k + 1, len(nums) - 1
        while i < j:
            sum_two = nums[i] + nums[j]
            if sum_two < target:
                i += 1
            elif sum_two > target:
                j -= 1
            else:
                if (nums[k], nums[i], nums[j]) not in r:
                    r.append((nums[k], nums[i], nums[j]))
                i += 1
                j -= 1
    return r


@pytest.mark.parametrize('nums, res', [
    ([-1, 0, 1, 2, -1, -4], [(-1, -1, 2), (-1, 0, 1)]),
    ([], []),
    ([0], []),
])
def test_three_sum(nums, res):
    assert three_sum(nums) == res
