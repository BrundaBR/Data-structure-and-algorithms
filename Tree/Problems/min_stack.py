class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        if self.stack!=[]:
            return self.stack.top()
        else:
            return 

    def getMin(self) -> int:
        if self.stack!=[]:
            # print(len(self.stack))
            min_val=min(self.stack)
            return min_val
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(7)
obj.pop()
print(obj.top())
print(obj.getMin())