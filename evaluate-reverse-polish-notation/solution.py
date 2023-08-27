class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        result_stack = []
        for token in tokens:
            #print(result_stack)
            if token == '+':
                result_stack.append(result_stack.pop() + result_stack.pop())
            elif token == '-':
                a,b = result_stack.pop(),result_stack.pop()
                result_stack.append(b-a)
            elif token == '*':
                result_stack.append(result_stack.pop() * result_stack.pop())
            elif token == '/':
                a,b = result_stack.pop(),result_stack.pop()
                result_stack.append(int(b/a))
            else:
                result_stack.append(int(token))
        return result_stack.pop()