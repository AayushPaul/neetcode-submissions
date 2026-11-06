class Solution:
    def climbStairs(self, n: int) -> int:
        #U: Return the number of distinct ways to climb to the top of the 
        # staircase. 
            # Climb with 1 or 2 steps at a time 
        
        #M/P: DP (bottom approach)
            # n = 5, array = [8, 5, 3, 2, 1, 1] #This means there are 8 distinct ways to climb to 5th step
            # (top of the staircase)

        #I: 
        one, two = 1, 1 

        for i in range(n - 1): 
            temp = one 
            one += two 
            two = temp 
        
        return one   

        #R: n = 5

        #E: O(n), Space: O(1)