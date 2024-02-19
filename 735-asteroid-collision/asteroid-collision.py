from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for asteroid in asteroids:
            if len(stack)==0:
                stack.append(asteroid)
            else:
                if stack[-1]>0 and asteroid <=0:
                    while stack[-1]>0 and asteroid <=0:
                        if abs(stack[-1]) < abs(asteroid):
                            stack.pop()
                        elif abs(stack[-1]) > abs(asteroid):
                            asteroid = None
                            break
                        else:
                            stack.pop()
                            asteroid = None
                            break
                        
                        if len(stack)==0:
                            stack.append(asteroid)
                            asteroid = None
                    if asteroid:
                        stack.append(asteroid)
                else:
                    stack.append(asteroid)
        return stack
