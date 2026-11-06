class Solution:
    #Time: 12:10 - 12:16 
    def search(self, nums: List[int], target: int) -> int:
        #U: Search for target within nums. If num exists, return index. Else, return -1. 
            # Array is already sorted in ascending order. 
            # Has to to run in O(logn) time 
        
        #M/P: 

        #I: 
        left, right = 0, len(nums) - 1

        while left <= right: 
            mid = (left + right) // 2

            if nums[mid] < target: 
                left = mid + 1
            elif nums[mid] > target: 
                right = mid - 1
            else: 
                return mid 
        
        return -1 

        #E: Time: O(n), Space: O(1) 