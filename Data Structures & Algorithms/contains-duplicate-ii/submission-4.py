class Solution:
    # Time: 11:20 - 
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # U: Return true if there are 2 distinct indices i and j in array such that nums[i] == nums[j
        # and abs(i - j) <= k

        # M/P: hashset 
            # On each iteration, move the right pointer. Move the left pointer when abs(i - j) > k 
            # and remove the orignal elem at left ptr from the window (left == i, right == j)

            # When nums[i] == nums[j], return True. 

        #I: 
        window = set()
        i = 0 

        for j in range(len(nums)): 
            if (abs(i - j) > k): 
                window.remove(nums[i])
                i += 1
            
            if nums[j] in window and abs(i - j) <= k: 
                return True 

            window.add(nums[j])

        return False 
        
        #R: nums = [1, 2, 3, 3], k = 3, output: true

        # window: set = (1, 2, 3, ) -> returns true 

        #E: Time: O(n), Space: O(n) 
            

        