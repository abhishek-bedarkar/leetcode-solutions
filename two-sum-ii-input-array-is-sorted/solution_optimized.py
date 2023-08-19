class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r,l = 0, len(numbers)-1

        while r < l:
            curr_sum = numbers[r] + numbers[l]

            if curr_sum == target:
                return [r+1,l+1]
            elif curr_sum < target:
                r+=1
            else:
                l -= 1