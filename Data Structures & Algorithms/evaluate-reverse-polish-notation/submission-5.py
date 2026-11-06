class Solution:
    # Time: 1:16 - 
    def evalRPN(self, tokens: List[str]) -> int:
        #U: Return the integer that represents the evaluation of the expression 

        #M/P: For loop that goes through each char in the tokens list 
            # Use stack 
            # When an operator is encountered, pop the top 2 elements/numbers and 
            # perform the operation on those numbers 
            # Add the new result to the stack 

            # Perform these actions each time an operator is encountered. 

        #Note: I don't have to consider the case where +, -, *, or / comes before the operands because RPN is postfix 
        # notation, not prefix notation. 

        #I: 
        stack = []
        for char in tokens: 
            if char == "+": 
                firstElem = stack.pop(-2)
                secondElem = stack.pop(-1)
                curResult = int(firstElem) + int(secondElem)
                stack.append(curResult)
            elif char == "-": 
                firstElem = stack.pop(-2)
                secondElem = stack.pop(-1)
                curResult = int(firstElem) - int(secondElem)
                stack.append(curResult)
            elif char == "*": 
                firstElem = stack.pop(-2)
                secondElem = stack.pop(-1)
                curResult = int(firstElem) * int(secondElem) 
                stack.append(curResult)
            elif char == "/": 
                firstElem = stack.pop(-2)
                secondElem = stack.pop(-1)

                # Note: valid expr is represented only; there is no need to consider the case 
                # where division by 0 error is present. 
                curResult = int(firstElem) / int(secondElem) 
                stack.append(curResult)
            else: 
                stack.append(char) 

        return int(stack[0]) 

        #R: tokens = ["1","2","+","3","*","4","-"]
            # stack = [5]
            # firstElem = stack.pop(-2) = 9
            # secondElem = stack.pop(-1) = 4
            # curResult = firstElem - secondElem = 5

            # Return stack[0] after going through all chars in tokens list with for loop 
        
        #E: Time: O(n), Space: O(n) 