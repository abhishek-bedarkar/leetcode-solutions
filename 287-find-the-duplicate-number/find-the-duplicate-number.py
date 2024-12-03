class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashmap = dict()

        for num in nums:
            if num in hashmap:
                return num
            else:
                hashmap[num] = 1
            
        