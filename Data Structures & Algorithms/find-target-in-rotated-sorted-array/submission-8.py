class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #U: Given the rotated sorted array nums and integer target, return 
        # index of target within nums or -1 if not present 

        #M/P: 
            #Binary Search 

        #I: 
        left, right = 0, len(nums) - 1
        
        while left <= right: 
            mid = (left + right) // 2

            if nums[mid] == target: 
                return mid 
            
            if nums[left] <= nums[mid]: # Search left portion of array
                if target > nums[mid] or target < nums[left]: 
                    left = mid + 1
                else: 
                    right = mid - 1
            else: # Search right portion of array
                if nums[mid] > target or target > nums[right]: 
                    right = mid - 1
                else: 
                    left = mid + 1
        
        return -1 

        #Time: O(logn), Space: O(1)