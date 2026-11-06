class Solution:
    # Time: 3:45 - 5:19 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #U: Group all anagrams together into sublists; I can return the output 
        # in any order. 

        #M/P: 
            # Sort the chars in each string in the strs array 
                # Make another array that has the sorted version of the strings 
            
            # Make a hashmap (keys are the sorted version of the strings, values: actual strings from the strs array that match the sorted version)

        #I: 
        hashmap = defaultdict(list)  

        for string in strs: 
            key = "".join(sorted(string)) # sorted(string) returns a list of chars in a string ('o', 'p', 's', 't')

            hashmap[key].append(string)
        
        return list(hashmap.values())

        #R: 
            # strs = ["act","pots","tops","cat","stop","hat"]
            # hashmap = {"act": ["act", "cat"], "opst": ["pots", "tops", "stop"], "aht": ["hat"]}
            # finalArr = [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]

        #E: Time: O(n * mlogm), Space: O(n * m) 