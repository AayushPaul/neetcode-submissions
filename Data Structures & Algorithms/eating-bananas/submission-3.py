class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #U: Piles[i] = # bananas in the ith pile 
            # h = number of hours you have to eat all the bananas 
            # k = bananas per hour eating rate 

            # Return the min eating speed (k) 

        #M/P:
            # Perform binary search on k values 
            # k can range from 1(left)  to max(piles) (right)

            # While left <= right: 
                # The initial value of k is (left + right) // 2. 
                # Keep track of the total time by going through the piles array; Add Math.ceil(p/k) 
                # to the total time 
                # If total time < h, try to make k even smaller by moving right to k - 1 and making the result = k 
                # If total time > h, try to make k larger by moving left to k + 1 

            # Return result 

        #I:  
        left, right = 1, max(piles) 
        result = right 

        while left <= right: 
            k = (left + right) // 2
            total = 0 

            for pile in piles: 
                total += math.ceil(pile / k)
            
            if total <= h: 
                result = k 
                right = k - 1
            else: 
                left = k + 1
        
        return result

        #Time: O(nlog(m)), Space: O(1)