class Solution:
    # Time: 10:39 - 
    def isValid(self, s: str) -> bool:
       #U: Given string s, return true if s is a valid string and false otherwise 

       #M/P: Initialize hashmap with close brackets as keys and corresponding open brackets
       # as values. 
        # Stack approach 

        #I: 
        openClosePairs = {")":"(", "]":"[", "}":"{"}
        stack = []

        for char in s:       
            if stack and char in openClosePairs: 
                poppedElem = stack.pop() 

                if poppedElem != openClosePairs[char]: 
                    return False 
            else: 
                stack.append(char) 

        return not stack

       #R: s = "]("

        # stack: ["]", "("]
        
       #E: Time: O(n)