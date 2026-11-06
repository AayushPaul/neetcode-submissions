class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #4:45 - 
        #U: Return the index of target in nums 
        # If it does not exist, return -1 

        #M/P: Binary Search 

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

        #R: 
        # nums = [1, 2, 3], target = 3

        #E: Time: O(log(n)), Space: O(1)