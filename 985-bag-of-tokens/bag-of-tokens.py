class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        max_score = 0
        while tokens:
            #print("power : ",power, "token :", tokens)
            # Face up
            if power > tokens[0]:
                val = tokens[0]
                tokens.remove(val)
                power -= val
                score += 1 

            # Face down
            elif score >= 1 and power > 0 and len(tokens) != 1:
                val = tokens[-1]
                tokens.remove(val)
                power += val
                score -= 1
            # break
            else:
                if power == tokens[0]:
                    val = tokens[0]
                    tokens.remove(val)
                    power -= val
                    score += 1
                else:
                    break
            max_score = max(score, max_score)
        return max_score

        