class Solution:
    # Time: 3:37 - 
    def characterReplacement(self, s: str, k: int) -> int:
        #U: You are given a string s consisting of only uppercase english characters. Choose up to 
        # k chars of the string and replace them with any other uppercase English character. 

        # After performing <= k replacements, return length of longest substring which contains only 
        # 1 distinct character 

        #M/P: Hashmap 

        #I: 
        left = 0
        res = 0 
        count = {} 

        for right in range(len(s)): 
            count[s[right]] = 1 + count.get(s[right], 0)

            if (right - left + 1) - max(count.values()) > k: 
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res

        #R: s = "ABABBA", k = 2
            # left, right = 1, 5

            # For loop (increments right ptr): 
                # count of elem at right ptr increases 
                # countA = 2, countB = 3

                # If (right - left + 1) - max(count.values) > k: 
                    # count of elem at left ptr decreases 
                    # left increments
                
                # res = max(res, right - left + 1)
            
            # res = right - left + 1
            # res is returned 
                
        #E: Time: O(n), Space: O(n) 
