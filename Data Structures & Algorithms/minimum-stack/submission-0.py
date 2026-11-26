class MinStack:

    def __init__(self):
        self.min_stack=[]
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.min_stack:
            return -1
        return self.min_stack[-1]
