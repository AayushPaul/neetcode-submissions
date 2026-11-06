class Solution:
    def isPalindrome(self, s: str) -> bool:
        #U: Given a string s, return true if it is a palindrome, 
        #otherwise, return false 

        #M: reversing string and determine if reversed string == s

        #P: 
            #1. Make all characters lower case(both s and reversedS) with Python lower function
            #2. Determine if reversedS == s; return true or false 
        
        #I:
        realS = ''
        for char in s: 
            if char.isalnum(): 
                realS += char.lower() #Returns new string with lower case chars(concatenation)

        return realS == realS[::-1] #Compares new string with reversed version of string

    #     l, r = 0, len(s) - 1

    #     while l < r:
    #         while l < r and not self.alphaNum(s[l]):
    #             l += 1
    #         while r > l and not self.alphaNum(s[r]):
    #             r -= 1
    #         if s[l].lower() != s[r].lower():
    #             return False
    #         l, r = l + 1, r - 1
    #     return True
    
    # def alphaNum(self, c):
    #     return (ord('A') <= ord(c) <= ord('Z') or 
    #             ord('a') <= ord(c) <= ord('z') or 
    #             ord('0') <= ord(c) <= ord('9'))