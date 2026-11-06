class Solution:
    def isValid(self, s: str) -> bool:
        #U: We have to determine if the string is valid 
            #1. Every open bracket is closed by the same type of bracket 
            # and in the correct order. 

            #2. Return true if these conditions are true; false otherwise
        
        #M: 
            #hashmap/dictionary to map the closing with the opening ones
            #Stack 
            #For each loop to go through each character in s
        
        #P: 
            #Create hashmap: [')': '(', etc]
            #Create a for each loop to go through each character 
            #Pop the last character in s and store that in a variable; 
            #Check if the key's value is in s 
        
        #I: 
        hashmap = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for char in s: 
            if char in hashmap: 
                if stack and stack[-1] == hashmap[char]: 
                    stack.pop() 
                else:
                    return False  
            else: 
                stack.append(char)
        
        if not stack: 
            return True 
        else: 
            return False 

        #R: Example 3

        #E: Time: O(n), Space: O(n)

        
            
