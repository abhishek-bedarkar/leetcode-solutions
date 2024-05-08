class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        result = []
        medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal' ]
        for i in range(len(score)):
            pos = sorted_score.index(score[i])

            if 0 <= pos <=2:
                result.append(medals[pos])
            else:
                result.append(str(pos+1))
        
        return result
        