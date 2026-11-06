class Solution:
    #Time: 11:06 - 11:53 
    def findMin(self, nums: List[int]) -> int:
        #U: The array is not sorted in ascending order; find the min element 

        #M/P: Binary Search 

        #I: 
        left, right = 0, len(nums) - 1

        while left < right: 
            mid = (left + right) // 2

            if nums[mid] > nums[right]: 
                left = mid + 1
            else: 
                right = mid # Don't do mid - 1 because mid could be the minimum (edge case) 

        return nums[left]

        #R: nums = [3, 4, 5, 6, 1, 2]
            # left, right = 4, 4
            # mid = (3 + 4) // 2 = 3 -> nums[3] = 6
            # if nums[mid] > nums[right] (6 > 1): 
                # left = mid + 1 = 4
            # else (1 <= 2)
                # right = mid = 4
            
            # return nums[left]
        
        #E: Time: O(logn), Space: O(1) 