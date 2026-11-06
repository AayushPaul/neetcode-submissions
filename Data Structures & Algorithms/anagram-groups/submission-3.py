class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #U: Given array of strings strs, group all anagrams together 
        #into sublists. Return output in any order. 

        #Anagram: exact same characters but the order 
        #of the characters can be different 

        #M: hashmaps, arrays 

        #P: 
            #1. Initialize hashmap and array
            #2. For each string in strs: 
                #3. For each char in string: 
                    #4. Increase count of hashmap[char] or each char
                #5. Compare hashmaps of each string 
            #4. Group strings together in [] when their hashmaps are equal; 
            # append those subarrays to array 
            #5. Return array 

      #I: 
        strings = {}
        array = []

        for string in strs: 
            sortedString = "".join(sorted(string)) #Counts as key; ensures it's a string

            if sortedString in strings: 
                strings[sortedString].append(string)
            else: 
                strings[sortedString] = [string]
            
        for value in strings.values(): 
            array.append(value)
            
        return array
        
            
            