class Solution:
    # Time: 12:21 - 12:40 
    def findDuplicate(self, nums: List[int]) -> int:
        #U: Find the duplicate number 

        #M/P: Slow and fast pointer method (Floyd's algorithm)

        #I: 
        slow, fast = 0, 0 
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: # (2 == 2)
                break 

        slow2 = 0 
        while True: 
            slow = nums[slow]   # 2
            slow2 = nums[slow2] # 2

            if slow == slow2: 
                return slow    #intersection happened again (definitely a duplicate: linked list cycle)

        #R: nums = [1, 2, 3, 2, 2]
            # hashmap = {1:1, 2:3, 3:1}

            # 2 is returned (duplicate)

        #E: Time: O(n), Space: O(1)