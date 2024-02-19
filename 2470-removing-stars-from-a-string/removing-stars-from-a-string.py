class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for elm in s:
            if elm == '*':
                stack.pop()
            else:
                stack.append(elm)
        return ''.join(stack)
                
        