class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #U: After performing k replacements, return the length of the longest substring which contains 
        # only one distinct character 

        #M/P: 
        # Sliding Window 

        # Initialize value of left pointer to 0. 
        # hashmap that keeps track of the frequency of each character 

        # Right pointer that goes through each char in string with a for loop 

        #I: 
        count = {}
        res = 0

        l = 0
        maxf = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res


