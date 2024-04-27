from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}
        positions = defaultdict(list)
        for i, c in enumerate(ring):
            positions[c].append(i)
        return self.calculateSteps(0, 0, positions, key, ring, memo)
    
    def calculateSteps(self, index, position, positions, key, ring, memo):
        if index == len(key):
            return 0
        if (index, position) in memo:
            return memo[(index, position)]
        min_steps = float('inf')
        for i in positions[key[index]]:
            if i >= position:
                steps = min(i - position, position + len(ring) - i)
            else:
                steps = min(position - i, i + len(ring) - position)
            min_steps = min(min_steps, steps + self.calculateSteps(index + 1, i, positions, key, ring, memo))
        memo[(index, position)] = min_steps + 1
        return min_steps + 1

        