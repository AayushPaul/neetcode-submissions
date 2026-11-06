class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #U: Given nums array, return output array where output[i] is product of all elems of nums except  
        # nums[i]

        #M/P: 
            # Create prefix and postfix arrays 
            # Modify the final result array based on different cases 
                # If i == 0, res[i] = 1 * postfix[i + 1] (one edge case) 
                # If i == len(nums) - 1, res[i] = prefix[i - 1] * 1 (another edge case)
                # res[i] = prefix[i - 1] * postfix[i + 1]

        #I: 
        res = [0] * len(nums) 
        prefix = [0] * len(nums) 
        postfix = [0] * len(nums) 
        prefixProduct, postfixProduct = 1, 1

        # Create the prefix array 
        for i in range(len(nums)): 
            prefixProduct *= nums[i]
            prefix[i] = prefixProduct 
        
        # Create the postfix array 
        for i in range(len(nums) - 1, -1, -1): 
            postfixProduct *= nums[i]
            postfix[i] = postfixProduct 

        # Modify the final result array based on 3 different cases 
        for i in range(len(nums)): 
            if i == 0: 
                res[i] = 1 * postfix[i + 1]
            elif i == len(nums) - 1: 
                res[i] = prefix[i - 1] * 1
            else: 
                res[i] = prefix[i - 1] * postfix[i + 1]
        
        return res

        #R: 
            # nums = [1, 2, 4, 6], 
            # prefix = [1, 2, 8, 48]
            # postfix = [48, 48, 24, 6] 
            # res = [48, 24, 12, 8]

        #E: Time: O(n), Space: O(n)



        
