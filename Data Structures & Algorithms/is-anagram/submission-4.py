class Solution:
    #Time: 11:33 - 
    def isAnagram(self, s: str, t: str) -> bool:
        #U: Given s and t, return true if two strings are anagrams of each
        # other. Otherwise, return False. 

        #M/P: 
        # If the length of the strings are NOT the same, return false 
        # Determine based on the frequency of chars (hashmaps)

        #I: 
        sMap = {} 
        tMap = {} 

        if len(s) != len(t): 
            return False 
        
        for char in s: 
            if char not in sMap: 
                sMap[char] = 1
            else: 
                sMap[char] += 1

        for char in t: 
            if char not in tMap: 
                tMap[char] = 1
            else: 
                tMap[char] += 1
    
        return sMap == tMap

        #Time: O(n), Space: O(n)