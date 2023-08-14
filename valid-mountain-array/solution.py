class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        ln = len(arr)
        if ln<=2:
            return False
        else:
            peak = max(arr)
            if arr.count(peak) >1 :
                return False
            if peak == arr[-1] or peak == arr[0]:
                return False
            else:
                ind = arr.index(peak)
                for i in range(0,ind):
                    if arr[i+1] <= arr[i]:
                        return False
                for i in range(ind,len(arr)-1):
                    if arr[i]<=arr[i+1]:
                        return False
                return True