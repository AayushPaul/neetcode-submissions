class Solution:
    # Time: 11:54 - 11:59 
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #U: Reverse a string; modify the input array in place with O(1) space memory 

        #M/P: Two Pointers Method 

        #I: 
        l, r = 0, len(s) - 1

        while l < r: 
            temp = s[l]
            s[l] = s[r]
            s[r] = temp 

            l += 1
            r -= 1
        
        return s

        #E: Time: O(n), Space: O(1)
