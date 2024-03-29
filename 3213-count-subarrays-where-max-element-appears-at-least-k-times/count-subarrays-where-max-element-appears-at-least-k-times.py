from collections import Counter
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num, l, cnt, result, left =max(nums), len(nums), 0, 0, 0

        for right in range(l):
            if nums[right]==max_num:
                cnt +=1

            while cnt >= k:
                if nums[left] == max_num:
                    cnt-=1
                left+=1

            result +=left
        return result




        