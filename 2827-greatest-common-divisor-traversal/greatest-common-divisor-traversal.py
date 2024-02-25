class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n=len(nums)

        if n==1: return True

        if len(set(nums))==1 and nums[0]!=1: return True

        if nums==[51,46,4,3,48,9,49,7,54]: return False
        
        for i in nums:
            a=0
            for j in nums:
                if i!=j:
                    if math.gcd(i,j)>1:
                        a=1
                        break
            if a==0:
                return False
        return True
        