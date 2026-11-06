class Solution:
    # Time: 1:22 - 2:14 (explained out loud - 4 min break)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #U: h = # hours I have to eat all the bananas 
            # piles[i] = # bananas in the ith pile
            # k = bananas/hr eating rate (I decide this)
        
        # Return the min integer k st I can eat all the bananas within h hours 

        #M/P: Sort the piles array 
            # Change the k value based on the total number of hours taken on each iteration of the binary 
            # search algorithm 

            # Normal while loop for the binary search (left <= right)
            # Have for loop inside the while loop to test each value in piles[i] with the current k value 
                # Use math.ceil function (piles[i] / k = # hrs to eat all the bananas in a pile)
                # Keep track of the total # hours on each iteration (add curr # hours from previous step to total)
            
            # If the total # hours > h, left = mid + 1
            # If the total # hours <= h: 
                # we have to keep track of the actual min integer k with the min function 
                # right = mid - 1

        #I: 
        left, right = 1, max(piles)
        minK = right

        while left <= right: 
            k = (left + right) // 2
            totalHrs = 0 

            for i in range(len(piles)): 
                pileHrs = math.ceil(piles[i] / k)
                totalHrs += pileHrs 
            
            if totalHrs > h: 
                left = k + 1
            else: 
                minK = k
                right = k - 1

        return minK

        # R: piles = [1,4,3,2], h = 9 
            # left, right = 2, 1
            # k = 1
            # totalHrs = 10
            # minK = 2, right = 1

            # 2 is returned 
        
        #E: Time: O(nlogm), Space: O(1) 
            # where n = size of input array, m = max value in array 
            