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

        # Ex: [1, 7, 3, 6, 5, 6], total = 28, check = 28 - 11 - 6 = 11
            # currSum = 11 
        
        #E: Time: O(n), Space: O(1) 