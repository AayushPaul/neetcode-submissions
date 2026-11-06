class Solution:
    # Time: 10:20 - 
    def validPalindrome(self, s: str) -> bool:
        #U: Return true if s can be a palindrome after deleting at most one character from it. 

        #M/P: Two Pointer Method 
            # Set the left and right ptrs 
            # while left < right
                # If chars at ptrs are same, move both ptrs 
                # If chars at ptrs are different, 
                    #1. string1 = [left:right], reversed1 = string1[::-1]
                    #2. string2 = [left + 1:right + 1], reversed2 = string2[::-1]

                    # Determine if either option results in a palindrome by comparing the reversed and normal
                    # strings. If either results in palindrome, return True. 
                    # If neither results in a palindrome, return False. 

        #I: 
        l, r = 0, len(s) - 1

        while l < r: 
            if s[l] != s[r]: 
                string1 = s[l:r]
                reversed1 = string1[::-1]

                string2 = s[l+1:r+1]
                reversed2 = string2[::-1]

                return string1 == reversed1 or string2 == reversed2
            else: 
                l += 1
                r -= 1
        
        return True

        #R: s = "abbda"
            # l, r = 0, len(s) - 1
            # l at b, r at d
            # Delete d, bb is a palindrome
                # Once we find the palindrome, we can return true. 
            
            # If all the chars are the same, return True after the while loop 
        
        #E: Time: O(n), Space: O(n)