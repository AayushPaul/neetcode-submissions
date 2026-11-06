class Solution:
    #Time: 2:01 - 2:40 
    def isAnagram(self, s: str, t: str) -> bool:
        #U: Return true if the 2 strings are anagrams of each other; return 
        # false otherwise 

        #M/P: 
            # Determine freq of characters in s and t and see if the hashmaps 
            # match 

        #I: 
        if len(s) != len(t): 
            return False 

        countS, countT = {}, {} 

        for charS in s: 
            if charS not in countS: 
                countS[charS] = 1
            else: 
                countS[charS] += 1
        
        for charT in t: 
            if charT not in countT: 
                countT[charT] = 1
            else: 
                countT[charT] += 1

        for char in countS:
            if countS[char] != countT.get(char, 0): 
                return False 
        
        return True

        #Time: O(n + m), Space: O(1)