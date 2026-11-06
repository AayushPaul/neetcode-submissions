class Solution:
    # Time: 5:39 - 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #U: Return true if s2 contains permutation of s1 or false otherwise. 
            # Other words: If permutation of s1 exists as substring of s2, return true. 
        
        #M/P: 
            # Have hashmap for s1 and s2
            # Sliding window comes in to preserve s1 as a substring of s2. 

            # First of all, we need to develop the s1 hashmap with all the frequencies 

            # Traverse through s2
                # When a s2 char is found in the s1 hashmap, left ptr moves to that char 
                # When the next char is NOT found in the s1 hashmap and length of s2 hashmap < length
                # of s1 hashmap, return False 

                # Otherwise, add chars to hashmap while length of s2 hashmap < length of s1 hashmap 
            
            # Compare the hashmaps (determine if each character has equal frequency)
            
        
        #I: 
        if len(s1) > len(s2):
            return False

        s1Map = {} 
        for char in s1: 
            s1Map[char] = 1 + s1Map.get(char, 0)
        
        for i in range(len(s2) - len(s1) + 1):
            s2Map = {}
            for j in range(i, i + len(s1)):
                char = s2[j]
                s2Map[char] = 1 + s2Map.get(char, 0)
            
            match = True
            for key in s1Map:
                if s1Map[key] != s2Map.get(key, 0):
                    match = False
                    break
            if match:
                return True
        
        return False

        #R: s2Map = {"c": 1, "a": 1, "b": 1}, match = True 
        # s1Map = {"a": 1, "b": 1, "c": 1}

        # True is returned

        #E: Time: O((len(s2) - len(s1)) * len(s1)), Space: O(n + m)