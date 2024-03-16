class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt_set = {}
        count = 0 
        result  = 0

        for i,num in enumerate(nums):
        
            if num == 0:
                count -= 1 
            else:
                count += 1
            
            if count == 0:
                result = max(result, i+1)
            elif count not in cnt_set:
                cnt_set[count] = i+1
            else:
                result = max(result, (i+1 - cnt_set[count]))
            #print("num :", num, " Count :", count, "result : ", result)
        #print(cnt_set)
        return result



        