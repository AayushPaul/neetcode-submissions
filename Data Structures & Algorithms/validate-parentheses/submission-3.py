class Solution:
    def isValid(self, s: str) -> bool:
        #Create a map of the elements 
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        #For-each loop 
        for char in s:     
            if char in closeToOpen: 
                if stack and stack[-1] == closeToOpen[char]: 
                    stack.pop() 
                else: 
                    return False 
            else: 
                stack.append(char)
            
        if not stack: 
            return True 
        else: 
            return False 
            
