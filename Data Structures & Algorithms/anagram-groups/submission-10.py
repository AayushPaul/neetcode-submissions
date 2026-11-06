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
        result = defaultdict(list)  

        for string in strs: 
            count = [0] * 26 

            for char in string: 
                count[ord(char) - ord("a")] += 1
            
            result[tuple(count)].append(string)
        
        return list(result.values())

        #R: 
            # strs = ["act","pots","tops","cat","stop","hat"]
            # result = {(1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1): ["act", "cat"], (tuple of count): ["pots", "tops", "stop"], tuple of count: ["hat"]}
            # finalArr = [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]

        #E: Time: O(n * m), Space: O(n * m) where n = # strings, m = length of the longest string