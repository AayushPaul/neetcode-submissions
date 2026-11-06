class Solution:
    # Time: 12:22 - 
    def isValid(self, s: str) -> bool:
       #U: String s is valid iff 
       #    1. Every open bracket is closed by the same type of close bracket 
       #    2. 

       #M/P: 

       #I: 
        closedOpen = {"}":"{", "]":"[", ")":"("}
        stack = [] 

        for char in s: 
            if stack and char in closedOpen and closedOpen[char] == stack[-1]: 
                stack.pop() 
            else: 
                stack.append(char)
                
        return True if not stack else False

        #R: s = "[(])"
            # stack = ["[", "(", "]", ")"]