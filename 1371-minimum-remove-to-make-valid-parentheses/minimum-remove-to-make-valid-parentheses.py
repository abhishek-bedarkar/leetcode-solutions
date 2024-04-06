class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i,c in enumerate(s):
            if c in ('(',')'):
                if len(stack) == 0:
                    stack.append(i)
                else:
                    if c=='(':
                        stack.append(i)
                    else:
                    
                        if s[stack[-1]] == '(':
                            stack.pop()
                        else:
                            stack.append(i)
        
        result = [s[i] for i in range(len(s)) if i not in stack]
        return ''.join(result)
                

        