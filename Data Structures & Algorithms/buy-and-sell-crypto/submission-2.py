class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        left, right = 0, 1
        profit = 0 

        while (right < len(prices)): 
            buy = prices[left] 
            sell = prices[right]

            if prices[right] <= prices[left]: 
                left = right 
            else: 
                profit = max(profit, sell - buy)

            right += 1 #right pointer will always move no matter what 
        
        return profit 