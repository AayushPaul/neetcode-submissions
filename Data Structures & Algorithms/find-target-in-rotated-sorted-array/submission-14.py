class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #U: Given array of length n, return index of target within nums or -1 
        # if not present. 

        #M/P: Binary Search - O(logn) 
            # left, right = 0, len(nums) - 1
            # while left <= right: 
                # mid = (left + right) // 2
                # If the mid number > target: 
                    # move right (left = mid + 1)
                    # repeat the process
                # If the mid number < target: 
                    # move left (right = mid - 1)
                    # repeat the process
                # Else: (mid number == target)
                    # Return mid index 

            # Return -1 when left > right  

        #I: 
        left, right = 0, len(nums) - 1

        while left <= right: 
            mid = (left + right) // 2

            if nums[mid] == target: 
                return mid 

            # Two Cases: when num at left ptr is > target and when num at left
            # ptr <= target (Array is sorted in ascending order) 
            if nums[left] <= nums[mid]: 
                if target < nums[left] or target > nums[mid]: #target should be in right portion
                    left = mid + 1
                else: 
                    right = mid - 1
            else: 
                if target > nums[right] or target < nums[mid]: #target should be in left portion
                    right = mid - 1
                else: 
                    left = mid + 1
        
        return -1

        #E: Time: O(logn), Space: O(1)