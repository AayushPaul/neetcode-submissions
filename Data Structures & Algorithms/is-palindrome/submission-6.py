class Solution:
    def isPalindrome(self, s: str) -> bool:
        #U: Given a string s, return true if it is a palindrome, 
        #otherwise, return false 
        
        #M: Two Pointers(left and right pointers)

        #P: 
            #1. left = 0, right = len(s) - 1
            #2. while left < right: 
                    #6. if char at left pointer != char at right pointer: 
                        #Return false 

                    #3. while left < right and the character at right index is not 
                    #alphanumeric: 
                        #right -= 1
                    
                    #4. while left < right and character at left index is NOT
                    #alphanumeric: 
                        #left += 1
                    
                    #5. left += 1, right -= 1 
            
            #7. Return true 

            #8. Create a separate function that determines if a character is alphanumeric
                #Upper case letter, lower case letter, or number 
            
        #I: 
        left, right = 0, len(s) - 1

        while left < right: 
            
            while left < right and not self.isAlphaNum(s[right]): 
                right -= 1
            
            while left < right and not self.isAlphaNum(s[left]): 
                left += 1
            
            if s[left].lower() != s[right].lower(): 
                return False 

            left += 1
            right -= 1
        
        return True 

    def isAlphaNum(self, c: str) -> bool: 
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
    
    #R: Example 1

    #E: Time: O(n), Space: O(1)
        
        
