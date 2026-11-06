class Solution: 
    # Time: 11:50 - 
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        #U: Return the longest common prefix of all the strings. If there is no longest common prefix, return an empty string ""  

        #M/P:  
         
        #I:  
        array = []  

        for i in range(len(strs)):  
            if i == 0:  
                array.append(strs[i]) 
            else:  
                j,k = 0,0 
                string = strs[i] # "abcd"
                arrString = array[-1] # ""
                newString = "" 

                while j < len(arrString) and k < len(string): 
                    if arrString[j] != string[k]:  
                        break 
                     
                    newString += string[k] 

                    j += 1 
                    k += 1 

                array.append(newString)

        return array[-1] if array else ""

        #R: strs=["abc","","abcd"]
            # array = ["abc", "", ""]
            # returns array[-1] == ""
        
        #E: Time: O(n * m), Space: O(n * m)
        