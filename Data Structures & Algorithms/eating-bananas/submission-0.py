class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) #speed(bananas/hour)
        result = right 
        
        while left <= right: 
            k = (left + right) // 2
            totalHours = 0 

            for pile in piles: 
                totalHours += math.ceil(float(pile) / k)
            
            if totalHours <= h: 
                result = k 
                right = k - 1
            else: 
                left = k + 1 #left > right at this point 
        
        return result 


            

