import pytest


def merge_sorted_inplace(nums1: list, m: int, nums2: list, n: int) -> None:
    """
    :param nums1: list of size m + n with ending with n * [0]
    :param nums2: list of size n
    :param m: number of non-zero integers in nums1
    :param n: number of integers in nums2
    """
    i, j = m - 1, n - 1
    for k in range(m + n - 1, -1, -1):  # reversed(range(m + n)):
        if j < 0:
            break
        elif i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1


@pytest.mark.parametrize('nums1, m, nums2, n, res', [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
])
def test_merge_sorted(nums1, m, nums2, n, res):
    merge_sorted_inplace(nums1, m, nums2, n)
    assert nums1 == res
