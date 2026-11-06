class Solution:
    # Time: 11:41 - 
    def evalRPN(self, tokens: List[str]) -> int:
        #U: Return the integer that represents the evaluation of the expression 

        #M/P: For loop to iterate through tokens list, Stack to keep track of curr nums/ops 
            # When + is encountered, add two prev elems in stack by popping them and get result; add result to the stack 
            # Do the same thing for * 
            # For - and /, order matters (NEED to have firstElem and secondElem vars, can also add these vars for +, *) 
        
        #I: 
        stack = [] 

        for char in tokens: 
            if char == "+": 
                secondElem = stack.pop() 
                firstElem = stack.pop() 
                res = int(firstElem) + int(secondElem) 
                stack.append(res) 
            elif char == "*": 
                secondElem = stack.pop() 
                firstElem = stack.pop() 
                res = int(firstElem) * int(secondElem)
                stack.append(res) 
            elif char == "-": 
                secondElem = stack.pop() 
                firstElem = stack.pop() 
                res = int(firstElem) - int(secondElem)
                stack.append(res) 
            elif char == "/": 
                secondElem = stack.pop() 
                firstElem = stack.pop() 
                res = int(firstElem) / int(secondElem)
                stack.append(res) 
            else: 
                stack.append(char)
        
        return int(stack[0])

        #R: tokens = ["1","2","+","3","*","4","-"]
            # stack = [5] # diff = firstElem - secondElem = 9 - 4 = 5
                         # When vals are popped, secondElem = 4, firstElem = 9
                         # Same thing happens for division (order matters) 9/4 != 4/9 (firstElem / secondElem)

        #E: Time: O(n), Space: O(n)