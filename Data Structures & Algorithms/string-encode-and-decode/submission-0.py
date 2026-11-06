class Solution:

    #Create your own algorithm(instructions do not tell you the exact way)
    def encode(self, strs: List[str]) -> str:
        fullString = ""

        for s in strs: 
            fullString += (str(len(s)) + "#" + s) #Length of s and # are eventually needed to decode the solution

        return fullString

    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while i < len(s): 
            j = i
            while s[j] != "#": 
                j += 1
            
            length = int(s[i:j])
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length 
        
        return result 