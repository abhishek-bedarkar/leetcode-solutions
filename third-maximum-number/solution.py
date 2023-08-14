class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)>= 3:
            res_list=[]
            [res_list.append(n) for n in nums  if n not in res_list]
            res_list.sort()
            if len(res_list)<=2:
                return max(res_list)
            return res_list[-3]
        else:
            return max(nums)