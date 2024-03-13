class Solution:
    def pivotInteger(self, n: int) -> int:
        i, j = 1, n
        left_sum, right_sum = i, j 
        while i <= j:
            #print(left_sum,' - ', right_sum)
            if left_sum == right_sum and i==j:
                return i
            elif left_sum <= right_sum:
                i += 1
                left_sum += i
            else:
                j -= 1
                right_sum += j

        return -1

        