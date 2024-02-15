class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sorted_sides = sorted(nums)
        sum_arr = [sum(sorted_sides[:2])]
        a = sum(sorted_sides[:2])
        for s in sorted_sides[2:]:
            sum_arr.append(a+s)
            a = a+s
        i=0
        print(sum_arr)
        print(sorted_sides)
        result = -1
        for i in range(len(sum_arr)-1):
            if sum_arr[i] > sorted_sides[i+2]:
                result = sum_arr[i+1]
        return result


        


