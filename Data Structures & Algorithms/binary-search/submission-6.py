class Solution:
    #Time: 1:55 - 2:07 (explained out loud)
    def search(self, nums: List[int], target: int) -> int:
        #U: Array is sorted in ascending order 
        # Find target within nums. If it exists, return index. If not, return -1. 

        #M/P: Binary Search 

        #I: 
        left, right = 0, len(nums) - 1

        while left <= right: 
            mid = (left + right) // 2

            if target > nums[mid]: 
                left = mid + 1
            elif target < nums[mid]: 
                right = mid - 1
            else: 
                return mid

        return -1

        #R: 
        # nums = [-1,0,2,4,6,8], target = 4
        # left, right = 3, 3
        # mid = (3 + 3) // 2 = 3
        # nums[mid] = 4
            # Since 4(target) == 4(value at mid ptr), target is found (return index of mid ptr == 3)
        
        #E: Time: O(logn), Space: O(1)