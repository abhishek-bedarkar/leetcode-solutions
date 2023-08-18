class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        for i in range(l-1):
            find = target - numbers[i]
            j = bin_search(numbers[i+1:], find)

            if j != -1:
                return [i+1,j+(l- len(numbers[i+1:]))+1]


def bin_search(arr, find):
    
    if len(arr) == 1 and find == arr[0]:
        return 0

    start = 0
    end = len(arr)
    mid = start + (end-start)//2

    while start < end:

        if arr[mid] == find:
            return mid
        elif arr[mid]>find:
            end = mid
        else:
            start = mid+1

        mid = start + (end-start)//2
    return -1