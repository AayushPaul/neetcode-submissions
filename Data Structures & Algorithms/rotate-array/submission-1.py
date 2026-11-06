class Solution:
    # Time: 12:35 - 1:24
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #U: Given nums, rotate array to the right by k steps 

        #M/P: Two Pointer strategy 
            # Right pointer is k places to the right of left pointer

        #I: 
        arrayCopy = []

        for num in nums: 
            arrayCopy.append(num) 

        k = k % len(nums)
        l, r = 0, k 

        while l < len(nums): 
            if r >= len(nums): 
                r = r % len(nums)

            nums[r] = arrayCopy[l]

            l += 1
            r += 1
        
        return nums

        #E: Time: O(n), Space: O(n)