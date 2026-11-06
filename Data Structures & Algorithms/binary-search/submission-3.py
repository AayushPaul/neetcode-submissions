class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #U: Search for target in nums and return its index 

        #M: Binary Search 

        #P: 
        
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

        #E: Time: O(log(n)), Space: O(1) 