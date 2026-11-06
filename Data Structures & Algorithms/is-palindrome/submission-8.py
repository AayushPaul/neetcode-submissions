class Solution:
    # Time: 1:34 - 
    def isPalindrome(self, s: str) -> bool:
        #U: Given a string s, return true if it is palindrome; return false 
            #Palindrome: Reads the same forward and backward; case-insensitive 
        
        #M/P: Two Pointers approach 
            # Left pointer moves towards the right 
            # Right pointer moves towards the left 

            # There should be a way to determine if a char is alphanumeric or non-alphanumeric (separate function)
            # making all chars lower case 

            # Edge cases: 
                # In the case where the character at the left or right ptr is NOT alphanumeric, then the respective 
                # ptr moves to the left or right 

                    # ex: If a question mark or space (non-alphanumeric char) is encountered at the right ptr but not at the 
                    # left ptr, then the right ptr moves to the left. 
                        # vice versa (same applies to when non-alphanumeric char is encountered at the left ptr)
                        # When non-alphanumeric chars are encountered at both pointers(ex: space), both the left and right ptrs move 

        #I: 
        left, right = 0, len(s) - 1

        while left < right: 
            while left < right and not self.isAlphanumeric(s[left]): 
                left += 1
            while left < right and not self.isAlphanumeric(s[right]): 
                right -= 1

            if s[left].lower() != s[right].lower(): 
                return False 

            left += 1
            right -= 1

        return True 

    def isAlphanumeric(self, char) -> bool: 
        return (ord('A') <= ord(char) <= ord('Z') or 
                ord('a') <= ord(char) <= ord('z') or 
                ord('0') <= ord(char) <= ord('9'))
        
        #E: Time: O(n), Space: O(1)