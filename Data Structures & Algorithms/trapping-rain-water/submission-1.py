class Solution:
    # Time: 11:30 - 12
    def trap(self, height: List[int]) -> int:
        #U: Return the max area of water that can be trapped in between the bars 

        #M/P: Two Pointer strategy 
            
        #I: 
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        area = 0 

        while left < right: 
            if maxLeft <= maxRight: 
                left += 1
                maxLeft = max(maxLeft, height[left])
                diff = maxLeft - height[left]
                area += diff
            else: 
                right -= 1
                maxRight = max(maxRight, height[right])
                diff = maxRight - height[right]
                area += diff 

        return area 

        #R: height = [0,2,0,3,1,0,1,3,2,1]
            # showed work in iPad 
        
        #E: Time: O(n), Space: O(1)