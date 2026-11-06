class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for string in strs: 
            count = [0] * 26 
            for s in string: 
                count[ord(s) - ord('a')] += 1
        
            ans[tuple(count)].append(string)
        
        return ans.values() 
