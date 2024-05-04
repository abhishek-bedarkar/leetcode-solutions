class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right, boats = 0, len(people)-1, 0
        
        while left <= right:
            
            # try to pair person with lowest and highest weight available
            if people[left] + people[right] <= limit:
                left += 1

            boats += 1
            right -= 1
        return boats
        