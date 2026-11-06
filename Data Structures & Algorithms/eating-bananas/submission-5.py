class Solution:
    # Time: 10:44 - 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #U: piles[i] = number of bananas in the ith pile 
            # h = # hours you have to eat all the bananas 
            # k = bananas/hr eating rate 
                # If pile has < k bananas, finish eating from that pile but do not eat from another pile. 

            # Return min integer k st you can eat all the bananas within h hours 

        #M/P: Binary Search 

        #I: 
        left, right = 1, max(piles) 
        k = 0 

        while left <= right: 
            mid = (left + right) // 2
            sumHrs = 0

            for elem in piles:  
                currTime = math.ceil(elem / mid)
                sumHrs += currTime 

            if sumHrs <= h:
                k = mid 
                right = mid - 1
            else: 
                left = mid + 1

        return k

        #R: piles = [1, 4, 3, 2], h = 9 
            # 1 hr + 2 hr + 2 hr + 1 hr = 6 hr < 9 hr 
            # k = 2 

            # binary search approach: 
                # l = 1, r = max(piles) 

                # while loop (l <= r)  
                    # mid = (l + r) // 2 

                    # for loop that goes through each elem in piles array 
                        # sum var initialized to 0 
                        # currTime = math.ceil(elem / k)
                        # sum += currTime 

                        #ex with for loop: sum = 0 + 1 + 4 + 3 + 2 = 10 > 9 (k = 1 does NOT work)
                    
                    # if sum <= h, r = k - 1 and ans = k
                    # l, r = 1, 1 

                    # if  sum > h, l = k + 1 and ans = k + 1
                    # l, r = 2, 1 (l > r, so program exits the while loop)

            # return ans 

        #E: Time: O(nlogm), Space: O(1)
