class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        mink_idx, maxk_idx, last_inv, result = -1,-1, -1, 0

        for i in range(len(nums)):
            if nums[i] == minK:
                mink_idx = i
            if nums[i] == maxK:
                maxk_idx = i

            if nums[i]< minK or nums[i] > maxK:
                last_inv = i
                mink_idx, maxk_idx = -1,-1


            if mink_idx != -1 and maxk_idx != -1:
                result += min(mink_idx, maxk_idx) - last_inv
                
            #print(f'mink_idx :{mink_idx}\t maxk_idx :{maxk_idx}\t last: {last_inv}\t result: {result}')
        return result

            
                



        