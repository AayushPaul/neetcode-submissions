class StockSpanner:
    # Time: 11:21 - 12:35 (watched video + 10 min break)

    # U: Span of stock's price in one day = max num of consec days (from that day and going backward) for which 
    # the stock price was <= price of that day 

        # Return the span of that stock's price for the current day 

    # M/P: 

    #I: 

    def __init__(self):
        self.stack = [] #pair: (price, span) 

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price: 
            span += self.stack[-1][1]
            self.stack.pop() 
        
        self.stack.append((price, span))
        return span 

    #R: arr = [100, 80, 60, 70, 60, 75]
        # stack = [(100, 1), (80, 1), (60, 1)[popped], (70, 2)[popped], (60, 1)[popped], (75, 4)]
        # Return span on each "next" function call 

    #E: Time: O(n), Space: O(n) 

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)