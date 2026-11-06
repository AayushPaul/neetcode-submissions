class Solution:
    # Time: 6:59 - 
    def search(self, nums: List[int], target: int) -> int:
        #U: Return the index of target within nums or -1 if not present 
            # Time Complexity: O(logn) 
        
        #M/P: Binary Search 

        #I: 
        left, right = 0, len(nums) - 1
        while left <= right: 
            mid = (left + right) // 2

            if target == nums[mid]: 
                return mid 

            #left sorted portion of array
            if nums[left] <= nums[mid]: 
                if target > nums[mid] or target < nums[left]: 
                    left = mid + 1
                else: 
                    right = mid - 1
            else: # right sorted portion of array
                if target < nums[mid] or target > nums[right]: 
                    right = mid - 1
                else: 
                    left = mid + 1
                
        return -1

        #R: nums = [3, 4, 5, 6, 1, 2], target = 1
            # 1st iteartion: 
                # l, r = 0, 5
                # mid = 2
                # l, r = 3, 5
            
            # 2nd iteration: 
                # l, r = 3, 5 
                # mid = 4 
                # nums[mid] == target (return mid)
                # 4 is returned 

            # nums = [9, 2, 5, 6, 7, 8], target = 7 

        #E: 