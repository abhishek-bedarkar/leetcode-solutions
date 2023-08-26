class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        code = {'(':1,
                '{':2,
                '[':3,
                ')':4,
                '}':5,
                ']':6}
        
        for elm in s:
            if code[elm]<=3:
                stack.append(code[elm])
            else:
                if len(stack) > 0:
                    if code[elm] == 4 and stack[len(stack)-1] == 1:
                        stack.pop()
                    elif code[elm] == 5 and stack[len(stack)-1] == 2:
                        stack.pop()
                    elif code[elm] == 6 and stack[len(stack)-1] == 3:
                        stack.pop()
                    else:
                        stack.append(code[elm])
                else:
                    stack.append(code[elm])

        if len(stack) == 0:
            return True
        else:
            return False