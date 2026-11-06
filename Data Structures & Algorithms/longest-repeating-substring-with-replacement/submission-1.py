class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #U: You are given a string s consisting of only uppercase english characters. Choose up to 
        # k chars of the string and replace them with any other uppercase English character. 

        # After performing <= k replacements, return length of longest substring which contains only 
        # 1 distinct character 

        #M/P: Hashset 

        #I: 

        #R: s = "XYYX", k = 1
            # count = {"X": 1, "Y": 2, }, maxf = 2, res = 3
        
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
