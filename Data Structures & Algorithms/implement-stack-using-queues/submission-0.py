class MyStack:

    def __init__(self):
        self.firstQueue = deque() #Stores elems in normal order (FIFO) 
        self.secondQueue = deque() #Stores elems in stack order (elements are dequeued/popped from the first queue and added 
                                    # to the second queue)

    def push(self, x: int) -> None:
        self.firstQueue.append(x) 
        poppedElem = self.firstQueue.popleft() 
        self.secondQueue.appendleft(poppedElem) 

    def pop(self) -> int:
        return self.secondQueue.popleft() 

    def top(self) -> int:
        return self.secondQueue[0] 

    def empty(self) -> bool:
        return False if self.secondQueue else True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

#R: firstQueue = (1, 2), secondQueue = (2, 1)   # Second queue is like the stack 