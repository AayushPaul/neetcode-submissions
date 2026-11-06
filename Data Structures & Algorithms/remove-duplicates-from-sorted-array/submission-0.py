class Solution:
    # Time: 11:20 - 
    def removeDuplicates(self, nums: List[int]) -> int:
        #U: Remove duplicates from nums in-place so that each element appears only once 
            # Return the number of unique elems (k) after removing the duplicates 
        
        #M/P: Two Pointer Approach
            # Initialize left pointer to 0, right pointer to index right after the left pointer 

            # While loop (left and right ptrs < len(nums)): 
                # If right ptr value == left ptr value, remove the value at the right ptr 
            
            # At the end, return the new length of nums array 

        #I: 
        if len(nums) == 1: 
            return 1 

        left, right = 0, 1

        while left < len(nums) and right < len(nums): 
            if nums[left] == nums[right]: 
                nums.remove(nums[right])    # removes the first occurence of the same value (removes the left ptr value)
            else: 
                left += 1
                right += 1
        
        return right 

        #R: nums = [2, 10, 40], len(nums) = 3
        # l = 2, r = 3
