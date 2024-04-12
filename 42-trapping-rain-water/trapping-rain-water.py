class Solution:
    def trap(self, height: List[int]) -> int:
        l, result = len(height), 0
        max_left, max_right = [0] * l, [0] * l

        max_left[0] = height[0]
        for i in range(1, l):
            max_left[i] = max(max_left[i - 1], height[i])

        max_right[l - 1] = height[l - 1]
        for i in range(l - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])

        for i in range(l):
            result += min(max_left[i], max_right[i]) - height[i]

        return result



        # level, flag, result  = max(height), True, 0

        # dp = [ [ 0 for j in range(len(height))] for i in range(level)]

        # for i in range(level):
        #     for j in range(len(height)):
        #         if height[j] != 0:
        #             dp[i][j] = 1
        #             height[j] -= 1

        # for i in range(level):
        #     left, right = 0,0
        #     while left < len(dp[i]):

        #         if dp[i][left] == 1:
                    
        #             right = left + 1
        #             count = 0
        #             while right < len(height) and dp[i][right] == 0:
        #                 count += 1
        #                 right += 1
                    
        #             if right < len(height):
        #                 result += count

        #             left = right

        #         else:
        #             left += 1
            #print(f'iteration:{i} level : {dp[i]}, result:{result}')
        


        return result

                    

            
            

        