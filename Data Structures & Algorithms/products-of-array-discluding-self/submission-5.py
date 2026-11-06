class Solution:
    #Time: 11:21- 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #U: Given nums, return output array where output[i] is the product of all the elems of nums except 
        # nums[i]

        #M/P: 

        #I: 
        prefix = [0] * len(nums) 
        postfix = [0] * len(nums) 
        result = [0] * len(nums)
        
        prefixProduct = 1
        for i in range(len(nums)):      
            prefixProduct *= nums[i]
            prefix[i] = prefixProduct
        
        postfixProduct = 1
        for j in range(len(nums) - 1, -1, -1):       
            postfixProduct *= nums[j]
            postfix[j] = postfixProduct

        for k in range(len(nums)): 
            if k == 0: 
                result[k] = 1 * postfix[k + 1] 
            elif k == len(nums) - 1: 
                result[k] = prefix[k - 1] * 1
            else: 
                result[k] = prefix[k - 1] * postfix[k + 1]
        
        return result

        #R: 
        # nums = [1,2,4,6] 
        # prefix =  [1, 2, 8, 48]
        # postfix = [48, 48, 24, 6]
        # result = [48, 24, 12, 8]

        #E: Time: O(n), Space: O(n) 