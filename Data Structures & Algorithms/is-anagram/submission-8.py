class Solution:
    #Time: 1:31 - 
    def isAnagram(self, s: str, t: str) -> bool:
        #U: Given 2 strings s and t, return true if 2 strings are anagrams of each other, 
        # return False 

            # Anagram: string that contains the exact same chars as another string, but 
            # the order of the chars can be different 
        
        #M/P: hashmap to store the # each char 
            # Check if the frequency of each char is equal in each string 
        
        #I: 
        sHashmap, tHashmap = {}, {} 

        for char in s: 
            if char in sHashmap: 
                sHashmap[char] += 1 
            else: 
                sHashmap[char] = 1
        
        for char in t: 
            if char in tHashmap: 
                tHashmap[char] += 1
            else: 
                tHashmap[char] = 1
        
        return sHashmap == tHashmap

        #R: 
        # s = "racecar", t = "carrace"
        
            # sHashmap = {"r": 2, "a": 2, "c": 2, "e": 1}
            # tHashmap = {"c": 2, "a": 2, "r": 2, "e": 1}
        
        #E: Time: O(n + m), Space: O(n + m)