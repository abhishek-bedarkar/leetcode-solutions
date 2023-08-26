class MinStack:
    soriginal_stack = None
    sorted_stack = None
    temp_stack = None

    def __init__(self):
        self.sorted_stack = []
        self.temp_stack = []
        self.original_stack = []

    def push(self, val: int) -> None:

        self.original_stack.append(val)

        if len(self.sorted_stack) == 0:
            self.sorted_stack.append(val)
        else:
            if val<= self.sorted_stack[len(self.sorted_stack)-1]:
                self.sorted_stack.append(val)
            else:
                while(val > self.sorted_stack[len(self.sorted_stack)-1]):
                    self.temp_stack.append(self.sorted_stack.pop())
                    if(len(self.sorted_stack)== 0):
                        break
                self.sorted_stack.append(val)
                
                while(len(self.temp_stack) != 0):
                    self.sorted_stack.append(self.temp_stack.pop())

    def pop(self) -> None:

        elm = self.original_stack.pop()
        self.sorted_stack.remove(elm)
        return elm

    def top(self) -> int:
        return self.original_stack[len(self.original_stack)-1]

    def getMin(self) -> int:
        #print(self.sorted_stack)
        return self.sorted_stack[len(self.sorted_stack)-1] 