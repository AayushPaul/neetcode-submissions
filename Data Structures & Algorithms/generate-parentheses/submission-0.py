class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open parentheses if open < n still 
        #only add closed parentheses if closed < open 
        #VALID if open == closed == n

        stack = []
        res = []

        def backtrack(openN, closedN): 
            if openN < n: 
                stack.append("(")
                backtrack(openN + 1, closedN) #Recursive call 
                stack.pop()

            if closedN < openN: 
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

            if openN == closedN == n: 
                res.append("".join(stack)) #Concatenates the elements of the stack into single strings in the res list 
                return 
        
        #initial value 
        backtrack(0, 0)
        return res

