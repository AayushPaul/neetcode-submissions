class Solution:
    def isValid(self, s: str) -> bool:
        #U: s is valid iff 
            # 1. Every open bracket is closed by same type of closed bracket 
            # 2. Open brackets are closed in correct order 
            # 3. Every close bracket has a corresponding open bracket of the same type.

            # Return true if s is valid string, false otherwise 
        
        #M/P: 
            # Intialize left ptr 
            # Initialize dictionary with key-value pairs (keys = closed bracket, values = open bracket) and stack 
            # Iterate through string with for loop 
            # As long as closing bracket is not encountered, keep adding opening brackets to stack 
            # Keep incrementing left ptr 
            # Once first closing bracket is encountered, exit for loop and enter while loop 

            # While stack is not null 
                # If value of elem at left ptr, which is in hashmap, is NOT equal to last elem in stack, return false 
                # Else, increment left ptr and pop elem from stack 
            
            # Return true 

        #I: 
        bracketPairs = {")":"(", "]":"[", "}":"{"}
        stack = []

        for char in s:
            if char in bracketPairs:
                if not stack or stack[-1] != bracketPairs[char]:
                    return False
                
                stack.pop()
            else:
                stack.append(char)
        
        return not stack

        #E: Time: O(n), Space: O(n) 