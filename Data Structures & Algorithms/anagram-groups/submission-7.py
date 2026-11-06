class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #U: Group all anagrams together into sublists; return output in any order 

        #M/P: 
            # Go through the strs array and sort each word 
                # The sorted word is the key. 
            
        #I: 
        resMap = defaultdict(list) 
        resArray = [] 

        for s in strs: 
            sortedS = ''.join(sorted(s))
            resMap[sortedS].append(s)
        
        return list(resMap.values()) 

        #R: Example 1 - resMap = {"act": ['act', 'cat'], "aht": ['hat'], 
            # "opst": ['pots', 'tops', 'stop']}
        
        #E: Time: O(n * mlogm), Space: O(n*m) where n is the number of strings and m is the 
        # length of the longest string. 