class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #U: Construct a new string by merging them in alternating order starting with word1
            # Take one character from word1 and then one from word2; repeat this process 

        #M/P: Two Pointers 
            # left (word1), right(word2) = 0, 0 
            # if len(word2) > len(word1): 
                # while l < len(word1) and r < len(word2): 
                    # Append char at left index first and then append char at right index 
                    # Move/increment the left and right ptrs 

                # Once left ptr is out of bounds, we only add the chars at right ptr 
                # to the final merged string. 

            # elif len(word1) > len(word2): 
                # while l < len(word1) and r < len(word2): 
                    # Append char at left index first and then append char at right index 
                    # Move/increment the left and right ptrs 

                # Once right ptr is out of bounds, we only add the chars at left ptr 
                # to the final merged string. 
            
            # else: 
                # while l < len(word1) and r < len(word2): 
                    # Append char at left index first and then append char at right index 
                    # Move/increment the left and right ptrs 

            #return output 

        #I: 
        l, r = 0, 0 
        finalStr = "" 

        if len(word2) > len(word1): 
            while l < len(word1) and r < len(word2): 
                finalStr += word1[l]
                finalStr += word2[r]

                l += 1
                r += 1
            
            finalStr += word2[r:len(word2)]
        elif len(word1) > len(word2): 
            while l < len(word1) and r < len(word2): 
                finalStr += word1[l]
                finalStr += word2[r]

                l += 1
                r += 1
            
            finalStr += word1[l:len(word1)]
        else: 
            while l < len(word1) and r < len(word2): 
                finalStr += word1[l]
                finalStr += word2[r]

                l += 1
                r += 1
        
        return finalStr

        #R: 
        # word1 = "ab", word2 = "abbxxc"
            # left, right = 0, 0 
            # Append char at left index first, append char at right index next 
            # mergedStr = "aabbbxxc"
        
        #E: Time: O(n + m), Space: O(n + m)