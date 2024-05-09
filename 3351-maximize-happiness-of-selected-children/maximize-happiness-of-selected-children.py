class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        max_happy = 0
        happiness.sort(reverse = True)

        for i in range(k):
            max_happy += max(happiness[i]-i,0)
            
        return max_happy
