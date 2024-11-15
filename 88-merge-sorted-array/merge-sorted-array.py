class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """

        left, right = m,0

        while right != n:
            nums1[left] = nums2[right]
            right += 1
            left += 1

        nums1.sort()