class Solution:
    #U: Encode a list of strings to a string; decode that string to the same list of 
    # strings 

    #M/P: 

    #I: 
    def encode(self, strs: List[str]): 
        encodedStr = []  
        for s in strs: 
            length = str(len(s)) 
            encodedStr.append(length + "#" + s)

        res = "".join(encodedStr)
        return res

    def decode(self, string: str): 
        finalList = [] 
        i = 0 

        while i < len(string): 
            j = i 
            while string[j] != "#": 
                j += 1
            
            length = int(string[i:j])
            word = string[j + 1 : j + 1 + length]
            finalList.append(word) 
            i = j + 1 + length
        
        return finalList

    #R: 
        # input = ["Hello", "Wor#ld"], res = "5#Hello6#Wor#ld"
            # encoded version = "5#Hello6#Wor#ld"
            # decoded version = ["Hello", ] -> "Hello" (indices 2-7 (2 + 5 = 7), 7 is excluded)

    #E: Time: O(n), Space: O(n) 