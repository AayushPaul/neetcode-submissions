class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       #U: Group all anagrams together into sublists. 

        #M/P: Use hashmap/default dictionary to store the keys (unique alphabetically sorted strings) and 
        # their values (each value is basically a subarray or sublist )

        #I: 
        anagramMap = defaultdict(list) # Either returns a default [] or it appends elements to the list

        for string in strs: 
            key = "".join(sorted(string)) #sorted(string) returns a list of the characters in sorted order.
            anagramMap[key].append(string)

        return list(anagramMap.values())

       #R: strs = ["act", "pots", "tops", "cat", "stop", "hat"] 
        # key1 = "act", value = ["act", "cat"]
        # key2 = "opst", value = ["pots", "tops", "stop"]
        # key3 = "aht", value = ["hat"]

        # hashmap = {"act": ["act", "cat"], "opst": ["pots", "tops", "stop"], "aht": ["hat"]}
        # Output = [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]

        #E: Time: O(n), Space: O(n)
