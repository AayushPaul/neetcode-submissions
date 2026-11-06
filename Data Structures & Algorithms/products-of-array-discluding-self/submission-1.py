class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)): 
            output[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): 
            output[i] *= postfix
            postfix *= nums[i]
        
        return output

        #R: Ex: [1, 2, 3, 4]

        #E: Time: O(n), Space: O(1)
