class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos =  [i for i in nums if i>=0]
        neg =  [i for i in nums if i<0]
        result = []
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        return result