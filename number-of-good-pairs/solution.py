class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_frequency = {}
        good_pairs_count = 0
        for num in nums:
            if num in num_frequency:
                good_pairs_count += num_frequency[num]
                num_frequency[num] += 1
            else:
                num_frequency[num] = 1

        return good_pairs_count