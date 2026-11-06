class Solution:
    #Time: 5:15 - 5:56 
    def maxArea(self, heights: List[int]) -> int:
        #U: Return the max amount of water a container can store. 

        #M/P: Two Pointers 
            # Initialize left and right ptrs
            # while left < right: 
                # if val at left ptr < val at right ptr, left ptr should get incremented 
                # if val at left ptr > val at right ptr, right ptr should get decremented 

                # Store the max amount of water using the max function
                    # Find the area of the rectangle/amount of water 
                        # width = right - left 
                        # height = min(height[left], height[right])
                        # area = max(area, width * height)
            
            # Return area
        
        #I: 
        left, right = 0, len(heights) - 1
        finalArea = 0 

        while left < right: 
            width = right - left #width = 3
            height = min(heights[left], heights[right]) #height = 2
            curArea = width * height 
            finalArea = max(finalArea, curArea) #area = 36, 6

            if heights[left] <= heights[right]: 
                left += 1
            else:
                right -= 1   

        return finalArea
        #R: height = [1, 4, 3, 5, 6], area = 12
                                 #L 
                                 #R
            
        #   height = [1, 6, 3, 5, 3], area = 10 
                        #L 
                        #R
        
        #E: Time: O(n), Space: O(1)