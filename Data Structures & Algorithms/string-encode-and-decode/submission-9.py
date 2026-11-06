class Solution:
    # Time: 11:20 - 11:55

    #U: Encode a list of strings to a string; decode that string to the same list of 
    # strings 

    #M/P: 

    #I: 
    def encode(self, strs: List[str]): 
        res = "" 

        for string in strs: 
            res += str(len(string)) + "#" + string

        return res 

    def decode(self, string: str): 
        resArr = [] 

        i = 0 
        while i < len(string): 
            j = string.find("#", i)
            length = int(string[i:j])
            resArr.append(string[j + 1 : j + 1 + length])
            i = j + 1 + length
        
        return resArr
    
    #R: input = ["#"]
        # string = "1##"
        # resArr = ["#"]
    
    #E: Time: O(n), Space: O(n)