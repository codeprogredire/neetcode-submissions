class MinStack:

    def __init__(self):
        self.stack = []
        self.topIndex = -1
        

    def push(self, val: int) -> None:
        if self.topIndex == -1:
            self.stack.append((val,val))
            self.topIndex += 1
        else:
            self.stack.append((val,min(val,self.stack[self.topIndex][1])))
            self.topIndex += 1
        

    def pop(self) -> None:
        self.stack.pop(self.topIndex)
        self.topIndex -= 1
        

    def top(self) -> int:
        return self.stack[self.topIndex][0]
        

    def getMin(self) -> int:
        return self.stack[self.topIndex][1]
