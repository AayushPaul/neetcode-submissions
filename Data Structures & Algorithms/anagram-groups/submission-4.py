class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #U: Given array of strs, group all anagrams together into sublists. 
        # You may return output in any order. 
            # Anagram: string that contains exact same chars as another string, 
            # but order of chars can be different 

        #M/P: 
            # For loop that goes through each string in strs array 
            # Sort each string in strs array and use join method; each 
            # unique string is a key. 

            # Append word matching the key to the same array 
            # Use defaultdict(list)
            # Create a hashmap for each unique string 

        #I: 
        ans = []
        hashmap = defaultdict(list) 

        for string in strs: 
            key = ''.join(sorted(string))
            hashmap[key].append(string)

        for value in hashmap.values(): 
            ans.append(value)

        return ans

        #R: 
            # Ex 1: 
                # hashmap = {'act': ['act', 'cat'], 'opst': ['pots', 'tops', 'stop'], 'aht': ['hat']}
                # ans = [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]

        #E: Time: O(m * nlog(n)), Space: O(m * n)