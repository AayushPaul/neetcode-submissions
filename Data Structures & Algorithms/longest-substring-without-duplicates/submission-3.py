class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #U: Find length of the longest substring without duplicate characters 

        #M/P: 
        # Use a set that keeps track of chars 
        # Iterate through the string with a for loop moving the right pointer 
        # Left pointer moves to where right pointer is if the current char is a duplicate or already appears
        # in the set 
        # Find the length of the substring by difference between the values for the left and right pointers
            # max function 
        
        # Return length 
         
        #Strategy: Sliding Window - the size of the window is basically the size of the substring; we have 
        # to find the longest possible size of the window or substring. 

        #I: 
        charSet = set() 
        left = 0 
        length = 0 

        for right in range(len(s)): 
            while s[right] in charSet: 
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            length = max(length, right - left + 1)
            
        return length

