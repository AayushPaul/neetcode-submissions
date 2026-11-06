class Solution:
    # Time: 9:46 - 
    def pivotIndex(self, nums: List[int]) -> int:
        #U: Calculate the pivot index of the array 
            # Return the leftmost pivot index. If no index exists, return -1. 
            # Pivot: Sum of all numbers strictly to the left = sum of all numbers strictly to the right 

        #M/P: One method is to sort and to use two pointers.
            # Another way is to find the sum of the whole array at the beginning. 
            # Use a pointer to keep track of the left sum. When total sum - left sum 

        #I: 
        currSum = 0
        total = sum(nums) 

        for i in range(len(nums)): 
            # Left sum is everything before the current index
            # Right sum is total - left sum - current element
            if currSum == total - currSum - nums[i]: 
                return i 
            currSum += nums[i]

        return -1

        # Ex: [3, 2, 5]
            # total = 10, currSum = 5, i = 1, check = 5