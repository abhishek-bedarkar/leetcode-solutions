from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        my_cnt = Counter(nums)
        dup = [k for k,v in my_cnt.items() if v ==2]
        nums = sorted(nums)
        missing=-1
        for i in range(1,len(nums)+1):
            if i not in nums:
                missing = i
                break
        return [dup[0],missing]