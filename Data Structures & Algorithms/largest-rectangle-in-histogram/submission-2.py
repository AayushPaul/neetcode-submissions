class Solution:
    # Time: 10:29 - 10:49
    def largestRectangleArea(self, heights: List[int]) -> int:
        #U: Return area of largest rectangle that can be formed among the bars. 
        # width of each bar is 1. 

        #M/P: Iterate through each bar and find the maximum width it can sustain
        maxArea = 0 
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h: 
                index, height = stack.pop() 
                maxArea = max(maxArea, height * (i - index))
                start = index

            stack.append((start, h))
        
        for i, h in stack: 
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea

        #E: Time: O(n), Space: O(n) 