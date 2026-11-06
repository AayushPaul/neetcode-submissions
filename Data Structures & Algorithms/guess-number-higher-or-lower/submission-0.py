# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    # Time: 3:00 - 
    def guessNumber(self, n: int) -> int:
        #U: Return number that I picked using the pre-defined guess function 

        #M/P: 

        #I: 
        l, r = 1, n 
        while True: 
            m = (l + r) // 2
            guessRes = guess(m) 

            if guessRes == -1: 
                r = m - 1
            elif guessRes == 1: 
                l = m + 1
            else:
                return m
 
        #R: n = 5, pick = 3 
            # l, r = 1, n = 5
            # m = (1 + 5) // 2, m = 3
            # My guess = 3, guessRes = 0
            # m is returned (3 is returned) because guessRes = 0 (my guess == pick) 
        
        #E: Time: O(logn), Space: O(1)