class Solution:
    def findMin(self, nums: List[int]) -> int:
        #U: Return min element of nums array in O(log(n)) time 

        #P: Binary Search 
            # Determine min element by 

        #I: 
        left, right = 0, len(nums) - 1
        minValue = nums[left]

        while left <= right: 
            if nums[left] < nums[right]: 
                minValue = min(minValue, nums[left])
                break 

            mid = (left + right) // 2
            minValue = min(minValue, nums[mid])

            if nums[mid] >= nums[left]: 
                left = mid + 1  #Search right 
            else: 
                right = mid - 1 #Search left 

        return minValue 

        #R: Example 2

        #E: Time: O(logn), Space: O(1)