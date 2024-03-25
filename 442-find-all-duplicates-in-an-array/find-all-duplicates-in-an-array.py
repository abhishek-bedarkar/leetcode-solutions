class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l = len(nums)

        temp = [0]*(l+1)

        result = []

        for num in nums:
            temp[num]+=1

        for i in range(len(temp)):
            if temp[i] > 1:
                result.append(i)

        return result