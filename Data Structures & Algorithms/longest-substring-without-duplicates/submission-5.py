class Solution:
    # Time: 10:14 - 11:07
    def lengthOfLongestSubstring(self, s: str) -> int:
        #U: Find length of the longest substring without duplicate chars 

        #M/P: Two Pointer Method and Hashset 
        # On each iteration, right ptr iterates 
        # On each iteration, char is added to hashset 
        # Keep track of max length of hashset (longest substring)

        # left pointer just moves when a duplicate/character already in set is found
            # The left pointer is moved to the index of that duplicate char 
            # Remove all chars in set when a duplicate char is found (use the clear method) 

        #Note: Is left ptr even needed? 

        #I: 
        substringSet = set() 
        maxLength = 0 
        left = 0 

        for right in range(len(s)): 
            while s[right] in substringSet: 
                substringSet.remove(s[left])
                left += 1

            substringSet.add(s[right])
            maxLength = max(maxLength, len(substringSet))

        return maxLength

        #E: Time: O(n), Space: O(n) 