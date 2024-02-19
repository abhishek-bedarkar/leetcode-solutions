class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        binary = bin(n)[2:]
        print(binary)
        if binary.count('1') == 1 and binary[0]=='1':
            return True
        else:
            return False
        