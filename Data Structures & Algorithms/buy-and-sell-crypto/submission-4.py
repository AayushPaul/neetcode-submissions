class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        #U: Choose single day to buy one NeetCoin and another day to sell it 
            #Return max profit you can achieve. 

        #M/P: Two Pointer Method 
            # If elem at left ptr is > elem at right ptr, move left ptr 
            # If elem at left ptr is <= elem at right ptr, move right ptr 
            # On each iteration, keep track of max profit and update it 

        #I: 
        left, right = 0, 1
        maxProfit = 0 

        while right < len(prices): 
            if prices[left] > prices[right]: 
                left = right 
            else: 
                currDiff = prices[right] - prices[left]
                maxProfit = max(currDiff, maxProfit)

            right += 1 
        
        return maxProfit

        #R: prices = [10, 1, 5, 6, 7, 1]
            # l, r = 1, 6
            # maxProfit = 6
        
        #E: Time: O(n), Space: O(1) 