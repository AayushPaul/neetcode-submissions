class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #U: Given nums array, return output array where output[i] is product of all elems of nums except  
        # nums[i]

        #M/P: 

        #I: 
        res = [] 
        for i in range(len(nums)): 
            product = 1 

            for j in range(len(nums)): 
                if i == j: 
                    continue 
                
                product *= nums[j]
            
            res.append(product)
        
        return res 

        #R: Example 2 - output: [0, ]
            # nums = [-1, 0, 1, 2, 3], res = [0, -6, 0, 0, 0]

        #E: Time: O(n^2), Space: O(n)
