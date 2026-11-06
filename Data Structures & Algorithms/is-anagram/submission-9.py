class Solution:
    #Time: 1:31 - 1:51 
    def isAnagram(self, s: str, t: str) -> bool:
        #U: Given 2 strings s and t, return true if 2 strings are anagrams of each other, 
        # return False 

            # Anagram: string that contains the exact same chars as another string, but 
            # the order of the chars can be different 
        
        #M/P: hashmap to store the # each char 
            # Check if the frequency of each char is equal in each string 
        
        #I: 
        sHashmap, tHashmap = {}, {} 
        
        if len(s) != len(t): 
            return False 

        for i in range(len(s)):  
            sHashmap[s[i]] = 1 + sHashmap.get(s[i], 0)
         
        for i in range(len(t)): 
            tHashmap[t[i]] = 1 + tHashmap.get(t[i], 0)
        
        return sHashmap == tHashmap

        #R: 
        # s = "racecar", t = "carrace"
        
            # sHashmap = {"r": 2, "a": 2, "c": 2, "e": 1}
            # tHashmap = {"c": 2, "a": 2, "r": 2, "e": 1}
        
        #E: Time: O(n + m), Space: O(k) or O(1) 