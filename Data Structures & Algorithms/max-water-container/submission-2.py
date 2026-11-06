class Solution:
    #Time: 9:54 - 10:23 
    def maxArea(self, heights: List[int]) -> int:
        #U: Return the max amount of water a container can store. 

        #M/P: Two Pointers 
            # Max amount of water: calculated with (right - left) * min(heights[left], heights[right])

            # On each iteration of the while loop, keep track of the current 
            # max amount of water with max function 
                # Remember to take the min value of the values at both ptrs 

        #I: 
        left, right = 0, len(heights) - 1
        maxAmt = 0 

        while left < right: 
            width = right - left 
            height = min(heights[left], heights[right])
            maxAmt = max(width * height, maxAmt)

            if heights[left] < heights[right]: 
                left += 1
            else: 
                right -= 1
        
        return maxAmt 

        #R: height = [1, 7, 2, 5, 4, 7, 3, 6]
            # left = 1, right = 5
            # width = 4 
            # height = 7
            # area = 28
            # maxAmt = max(28, 36) = 36
        
        #E: Time: O(n), Space: O(1)