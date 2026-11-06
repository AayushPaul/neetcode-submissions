class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #U: Given two strings(s and t), return true if 
        #these 2 strings are anagrams of each other; return false 
        #Anagram: exact same chars, but order can be different

        #M: Hashmap, for loops, conditionals 

        #P: Count the # occurences of each unique character 
            #1. Check if the length of both strings are equal 
            #2. Create two hashmaps(one for each string)
            #3. Add each character to each hashmap 
            #4. Check if the # occurences is the same for each string 
            #5.     If the # occurrences is the same, program returns true 
            #6. After for loop, program returns false 

        #I: 
        if len(s) != len(t): 
            return False  
        
        sMap = {} #characters and their counts
        tMap = {}

        for char in s: 
            sMap[char] = 1 + sMap.get(char, 0) 
        
        for char in t: 
            tMap[char] = 1 + tMap.get(char, 0)

        return sMap == tMap 

        #R: Example 2

        #E: Time: O(N + M), Space: O(N + M)

        