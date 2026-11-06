class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #U: Remove all occurences of val from nums in place 
            # Return the number of remaining elems 
            # (forgot this part: The first k elements of nums do not 
            # contain val)

        #M/P: 
            # Initialize k to 0. 
            # Iterate through the nums array with a for loop (i) 
                # if nums[i] != val, swap the value at the kth index 
                # with the value at the ith index and increase k. 

            # The elements beyond the first k positions do not need to be 
            # considered. Thus, return k after for loop. 

        #I: 
        k = 0 
        for i in range(len(nums)): 
            if nums[i] != val: 
                nums[k] = nums[i]
                k += 1

        return k 

        #R: 
            # nums = [1, 1, 2, 3, 4], val = 1
            # output: k = 0, i = 2 -> [2, 1, 2, 3, 4], k = 1
                #     k = 1, i = 3 -> [2, 3, 2, 3, 4], k = 2
                #     k = 2, i = 4 -> [2, 3, 4, 3, 4], k = 3

                # Return k (3) 
        
        #E: Time: O(n), Space: O(1)