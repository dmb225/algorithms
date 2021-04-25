import pytest
from typing import List


def maximum_sub_product(nums: List[int]) -> int:
    """
    :param nums: a list of integer
    :return: the sum of nums's subarray which has the largest product
    """
    if not len(nums):
        return 0
    max_prod, min_prod = nums[0], nums[0]
    result = max_prod
    for i in range(1, len(nums)):
        num = nums[i]
        temp_max = max(num, max_prod * num, min_prod * num)
        min_prod = min(num, max_prod * num, min_prod * num)
        max_prod = temp_max
        result = max(result, max_prod)
    return result


@pytest.mark.parametrize('nums, res', [
    ([2, 3, -2, 4], 6),
    ([9, 1, 0, -5, -2], 10),
])
def test_maximum_sub_product(nums, res):
    assert maximum_sub_product(nums) == res
