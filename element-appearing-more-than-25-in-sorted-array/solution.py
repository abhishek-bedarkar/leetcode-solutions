class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = len(arr)//4
        curr = 1
        i=0
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                curr += 1
            elif curr > freq:
                return arr[i]     
            else:
                curr = 1
        return arr[i] 