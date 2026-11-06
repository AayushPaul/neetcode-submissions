class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Time: 12:19 - 12:37 (explaining out loud)

        #U: Return index if target is found in sorted array. If target not found, return index where it would be if 
        # target was inserted in order 

            # Time complexity : O(logn) 
        
        #M/P: 

        #I: 
        left, right = 0, len(nums) - 1

        while left <= right: 
            mid = (left + right) // 2

            if nums[mid] < target: 
                left = mid + 1
            elif nums[mid] > target: 
                right = mid - 1
            else: #nums[mid] == target
                return mid 
        
        if nums[mid] < target: 
            return mid + 1
        else: # nums[mid] > target  
            return mid

        #R: nums = [-1, 0, 2, 4, 6, 8], target = 5

        # l = 0, r = len(nums) - 1
        # while l < r: 
            # mid = (l + r) // 2
            # mid at 2, left at 4   (nums[mid] < target)
            # mid at 6, right at 4  (nums[mid] > target)
            # mid at 4 (index 3), left at 6  (left > right, so program exits the while loop)

            #Note: At any point in the while loop, if target is found, return mid index (nums[mid] == target)
        
        # return mid + 1 (index to the right of the mid index)
        # return 3 + 1 = 4

        #E: Time: O(logn), Space: O(1)