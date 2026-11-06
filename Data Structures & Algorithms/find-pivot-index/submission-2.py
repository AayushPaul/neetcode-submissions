class Solution:
    # Time: 10:42 - 11:22
    def pivotIndex(self, nums: List[int]) -> int:
        #U: Given nums, calculate pivot index of this array 
            # Pivot index: sum of all elems strictly to the left of the index = sum of all elems strictly to
            # the index's right 

            # If index is on the left edge of the array, left sum is 0 because there are no elems to the left. 
            # This also applies to the right edge of the array. 

            # Return leftmost pivot index 

        #M/P: 
            # Determine sum of nums array 
            # Iterate through nums array with for loop 
                # Keep track of leftSum and rightSum at each index 
                # When leftSum == rightSum, return index 
            
            # Return -1 after for loop (if no point is encountered where leftSum == rightSum)
        
        #I: 
        total = sum(nums) 
        leftSum = 0 

        for i in range(len(nums)): 
            rightSum = total - leftSum - nums[i]

            if leftSum == rightSum: 
                return i 

            leftSum += nums[i]
        
        return -1 

        #R: 
            # nums = [1, 7, 3, 6, 5, 6]

            # total = 28, leftSum = 0, rightSum = 28 - 0 - 1 = 27 

            # total = leftSum + rightSum + nums[i] = 28, leftSum = 1, 
                # rightSum = total - leftSum - nums[i] = 28 - 1 - 7 = 20
            
            # total = 28, leftSum = 8, rightSum = 28 - 8 - 3 = 17 
            # total = 28, leftSum = 11, rightSum = 28 - 11 - 6 = 11 (leftSum == rightSum at index 3)

            # Return 3 

            # nums = [1]
                # total = 1, leftSum = 0, rightSum = 1 - 0 - 1 = 0 
                # Return 0 (pivot index = 0)

        #E: Time: O(n), Space: O(1) 