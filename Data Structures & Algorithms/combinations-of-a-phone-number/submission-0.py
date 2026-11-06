class Solution:
    # Time: 12:55 - 1:59 
    def letterCombinations(self, digits: str) -> List[str]:
        #U: Digits (2 - 9)
            # Each digit (not including 1) is mapped to a set of chars 
            # Return the possible letter combinations that digits could represent; return answer in any order 
        
        #M/P: 
            # Hashmap (stores digits and the letters they map to) 
            # Backtrack function 

        
        #I: 
        if not digits:
            return []

        hashmap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = [] 

        def backtrack(i, currSubstr):
            if len(currSubstr) == len(digits): 
                result.append(currSubstr)
                return
            
            for char in hashmap[digits[i]]: 
                backtrack(i + 1, currSubstr + char)
        
        backtrack(0, "")
        return result

        #R: digits = "345"
            # ["d"]
            # result = 

        #E: 