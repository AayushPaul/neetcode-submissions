class Solution:
    # Time: 10:29 - 10:49
    def largestRectangleArea(self, heights: List[int]) -> int:
        #U: Return area of largest rectangle that can be formed among the bars. 
        # width of each bar is 1. 

        #M/P: Iterate through each bar and find the maximum width it can sustain
        maxArea = 0 
        n = len(heights)

        for i in range(n):
            # Find the leftmost index where heights[left] >= heights[i]
            left = i
            while left > 0 and heights[left - 1] >= heights[i]:
                left -= 1
            
            # Find the rightmost index where heights[right] >= heights[i]
            right = i
            while right < n - 1 and heights[right + 1] >= heights[i]:
                right += 1
            
            # Width is (right - left + 1)
            currArea = heights[i] * (right - left + 1)
            maxArea = max(maxArea, currArea)
        
        return maxArea