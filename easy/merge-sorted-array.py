"""
Solve for Leetcode Merge Sorted Array
Difficulty: Easy

Problem Statement
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
    Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -10^9 <= nums1[i], nums2[j] <= 10^9
Solution1 using bisect and list.insert Complexity O(n*(m+log(m)))
Solution2 using direct comparisons between elements of nums1 & nums2 Complexity O(2m+n)
"""
import bisect
from typing import List


class Solution:
    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # the complexity of this operation can be ignored since it will be added to a much bigger term
        del nums1[m:m + n]

        # Iterates n times hence the complexity is O(n*(X)) when X is the complexity for what happens inside the loop
        for element in nums2:
            # the bisection happens first and that's O(log(m))
            # then the insertion and that's O(m)
            # So X = log(m) + m
            nums1.insert(bisect.bisect_left(nums1, element), element)


class Solution2:
    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # the complexity of this operation id O(m)
        a = nums1[:m]
        i, j = 0, 0
        # The complexity of this algorithm lies in this loop since it iterates m+n -> Complexity O(n+m)
        for k in range(0, m+n):
            if i == m:
                nums1[k] = nums2[j]
                j += 1
                continue
            if j == n:
                nums1[k] = a[i]
                i += 1
                continue
            if a[i] < nums2[j]:
                nums1[k] = a[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
