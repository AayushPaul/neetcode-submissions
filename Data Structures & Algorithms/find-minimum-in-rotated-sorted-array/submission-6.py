class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r: 
            if nums[l] <= nums[r]: 
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]: 
                l = mid + 1
            else: 
                r = mid - 1
            
        return res

        #R: Example 2 - nums = [4, 5, 0, 1, 2, 3]
            # left, right = 0, 5, mid = (0 + 5) // 2 = 2
            # res = min(4, 0), res = 0 
            # right = 1, res = 0
        
        #E: Time: O(logn), Space: O(1)
