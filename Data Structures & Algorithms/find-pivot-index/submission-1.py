class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #U: Given nums, calculate pivot index of this array 
            # Pivot index: sum of all nums strictly to the left of the index = sum of all nums strictly
            # to the index's right 

            # Return leftmost pivot index; if no such index, return -1 

        #M/P: 
            # Find the total sum of all nums using the sum func

            # Keep track of the left and right sum values 
            # Go through nums array with a normal for loop 
                # rightSum = total - leftSum - nums[i]
                # At any point, if leftSum == rightSum, return index (i) 
                # Increase leftSum normally (accumulation)
                

        #I: 
        total = sum(nums) 
        leftSum = 0 

        for i in range(len(nums)): 
            rightSum = total - leftSum - nums[i]
            if leftSum == rightSum: 
                return i 
            
            leftSum += nums[i]
        
        return -1 

        #R: Example 3 - nums = [2, 1, -1], total = 2
            #leftSum = 0, rightSum = total - leftSum - nums[i] = 2 - 0 - 2 = 0 
            # Since leftSum = rightSum, 0 (i) is returned. 

        #   Example 2 - nums = [3, 2, 1], total = 6 
            #leftSum = 0, rightSum = 6 - 0 - 3 = 3 
            # leftSum = 3, rightSum = 6 - 3 - 2 = 1 
            # leftSum = 5, rightSum = 6 - 5 - 1 = 0 

            # -1 is returned 

        #E: Time: O(n), Space: O(1)
