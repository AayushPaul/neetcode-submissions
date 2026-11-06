class Solution:
    # Time: 3:58 - 4:29 
    def mySqrt(self, x: int) -> int:
        #U: Return the sqrt(x) rounded down to the nearest integer; the returned integer should be 
        # non-negative as well 

        #M/P: 

        #I: 
        l, r = 1, x 

        while l <= r: 
            m = (l + r) // 2
            currSquared = m * m 

            if currSquared < x: 
                l = m + 1
            elif currSquared > x: 
                r = m - 1 
            else: 
                return m # Perfect square case(ex: x = 9, m = 3)
        
        return r # Imperfect square case (ex: x = 13, r = 3)

        #R: x = 13
            # ex: 3^2 == 9, 4^2 == 16, ans = 3
            # l = 1, r = x = 13, m = 7, m^2 = 7^2 = 49 > 13 
            # r = m - 1 = 7 - 1 = 6
            # l = 1, r = 6, m = (1 + 6) // 2 = 3, m^2 = 3^2 = 9 
            # l = m + 1 = 3 + 1 = 4
            # l = 4, r = 6, m = (4 + 6) // 2 = 5, m^2 = 5^2 = 5 * 5 = 25 
            # r = m - 1 = 5 - 1 = 4 
            # l = 4, r = 4, m = (4 + 4) // 2 = 4, m^2 = 4^2 = 16 
            # r = m - 1 = 4 - 1 = 3
            # l = 4, r = 3 (since l > r, program exits the while loop)
        
            # Return r 
        
        #E: Time: O(logn), Space: O(1)