class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #U: Given piles, h is the # hours we have to eat all the bananas in 
        # Return the min integer k such that I can eat all the bananas
        # within h hours; k = bananas/hour 

        #M/P: Binary Search 
            # left = 1, right = max num in piles 
            # res = right 

            # while left <= right: 
                # k should be the mid ptr: (left + right) // 2
                # totalTime = 0

                # For loop that goes through the piles array and 
                # gets the total time
                    # totalTime += Math.ceil(elem/k)
                
                # If total time > h, left = k + 1
                # If total time < h, res = k, right = k - 1

        #return result 

        left, right = 1, max(piles) 
        res = right 

        while left <= right: 
            k = (left + right) // 2
            totalTime = 0 

            for p in piles: 
                totalTime += math.ceil(p/k)
            
            if totalTime > h: 
                left = k + 1
            else:
                res = k 
                right = k - 1

        return res 

        #E: Time: O(n*logm), Space: O(1)