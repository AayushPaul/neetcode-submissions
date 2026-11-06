class Solution:
    # Time: 6:40 - 

    #U: Implement functionality for encoding and decoding strings 

    #M/P: 

    #I: 
    def encode(self, strs: List[str]): 
        encodedStr = ""
        for string in strs: 
            length = len(string) 
            encodedStr += str(length) + "#" + string 

        return encodedStr 

    def decode(self, string: str): 
        resultArr = [] 
        i = 0 

        while i < len(string): 
            j = i 

            while string[j] != "#": 
                j += 1
            
            length = int(string[i:j])
            i = j + 1
            j = i + length 
            word = string[i:j] #Hello
            resultArr.append(word) 

            i = j
        
        return resultArr 

    #R: input = ["Hello", "World"]
    # Encoded version: "5#Hello5#World"

    # Decoded version: decoded(encoded string) = ["Hello", "World"]

    #E: Time: O(n), Space: O(n)