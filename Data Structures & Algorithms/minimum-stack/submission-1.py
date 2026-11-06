class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        minStackValue = 0
        self.stack.append(val)
        if self.minStack: 
            minStackValue = self.minStack[-1]
        else: 
            minStackValue = val

        val = min(val, minStackValue)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop() 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
