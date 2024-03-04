class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        max_score = 0

        # brute force approach
        # while tokens:
        #     #print("power : ",power, "token :", tokens)
        #     # Face up
        #     if power > tokens[0]:
        #         val = tokens[0]
        #         tokens.remove(val)
        #         power -= val
        #         score += 1 

        #     # Face down
        #     elif score >= 1 and power > 0 and len(tokens) != 1:
        #         val = tokens[-1]
        #         tokens.remove(val)
        #         power += val
        #         score -= 1
        #     # break
        #     else:
        #         if power == tokens[0]:
        #             val = tokens[0]
        #             tokens.remove(val)
        #             power -= val
        #             score += 1
        #         else:
        #             break
        #     max_score = max(score, max_score)
        # return max_score

        # Two pointers approach
        left = 0
        right = len(tokens)-1
        tokens.sort()
        while left <= right:
            #print("power : ",power, "token :", tokens[left:right+1])
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left += 1
            elif score >= 1:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                break
            max_score = max(score, max_score)
        return max_score
         

        