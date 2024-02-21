class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        counter = 0
        while left != right:
            left >>= 1
            right >>= 1
            counter += 1
        
        right <<= counter
        return right
            
        