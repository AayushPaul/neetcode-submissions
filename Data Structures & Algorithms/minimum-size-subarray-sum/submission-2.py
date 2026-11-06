class Solution:
    #Time: 10:49 PM - 
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #U: Return the minimal length of subarray whose sum is >= target. If there is no such subarray, return 0. 

        #M: Sliding Window 

        #P: 
        # l, total variables 
        # minLength with min keyword 
        
        #I: 
        l, total = 0, 0
        minLength = float('inf')

        for r in range(len(nums)): 
            total += nums[r]

            while total >= target:
                minLength = min(minLength, r - l + 1) 
                total -= nums[l]
                l += 1

        return minLength if minLength != float('inf') else 0

        #R: target = 10, nums = [2, 1, 5, 1, 5, 3]
            # minLength = 3
            # l, r = 3, 5
            # total = 9
            

        #E: Time: O(n), Space: O(1)