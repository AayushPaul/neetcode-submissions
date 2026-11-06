class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs: 
            count = [0] * 26

            for char in string: 
                count[ord(char) - ord("a")] += 1
            
            #strings with same counts of each character are added to the same group
            result[tuple(count)].append(string)
        
        return result.values()
                
