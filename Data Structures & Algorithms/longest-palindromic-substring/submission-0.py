class Solution:
    def longestPalindrome(self, s: str) -> str:
        #U: Return the longest palindromic substring in s. 

        #M/P: Two Pointer/Sliding Window Method 

        #I: 
        res = ""
        resLen = 0 

        for i in range(len(s)): 
            #curr resLen = 2

            #odd length 
            l, r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if (r - l + 1) > resLen: 
                    res = s[l:r+1]
                    resLen = r - l + 1
                
                l -= 1
                r += 1
            
            #even length 
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if (r - l + 1) > resLen: 
                    res = s[l:r+1]
                    resLen = r - l + 1
                
                l -= 1
                r += 1

        return res