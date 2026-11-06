class Solution:
    # Time: 11:26 - 11:57 
    def isPalindrome(self, s: str) -> bool:
        #U: Given a string s, return true if it is palindrome; return false 
            #Palindrome: Reads the same forward and backward; case-insensitive 

        #M/P: 
            # Two Pointers method 
                # Compare each character at left and right ptrs in while loop 
                # Make each char lowercase. 

                # When a non-alphanumeric char (ex: space) is encountered, then move the pointer 
                # at the space only 

            # Define a separate function that determines if a char is alphanumeric (A-Z, a-z, 0-9) 
        
        #I: 
        left, right = 0, len(s) - 1

        while left < right: 
            if not self.isAlphaNum(s[left]): 
                left += 1
            elif not self.isAlphaNum(s[right]): 
                right -= 1
            elif not self.isAlphaNum(s[left]) and not self.isAlphaNum(s[right]): 
                left += 1
                right -= 1
            else: 
                if s[left].lower() != s[right].lower(): 
                    return False 
                else: 
                    left += 1
                    right -= 1
        
        return True 
    
    def isAlphaNum(self, c: char) -> bool: 
        return ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9')

    #E: Time: O(n), Space: O(1)