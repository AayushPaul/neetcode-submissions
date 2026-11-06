class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #U: Given s and t, return true if 2 strings are anagrams of each other
        # Else, return False 

        #M/P: 
            # Use hashmap to determine the frequency of characters 
                # Note: Hashmaps will always have the max size of 26 chars since
                # s and t only have lowercase English letters; Space: O(1) 

            # Return True if the hashmaps are equal; else, return False 
        #I: 
        countS, countT = {}, {} 

        if len(s) != len(t): 
            return False 

        for i in range(len(s)): 
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT

        #Time: O(n + m), Space: O(1)