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
        # for i in range(len(prices)): 
        #     buy = prices[i]
        #     for j in range(i + 1, len(prices)):
        #         sell = prices[j] 
        #         profit = max(profit, sell - buy)
        
        # return profit 