class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd_list = [num for num in nums if num%2 ==1 ]
        even_list = [num for num in nums if num%2 ==0 ]
        return even_list + odd_list