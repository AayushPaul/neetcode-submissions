class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #U: Return the integer that appears more than once 

        #M/P: Linked List Cycle Problem (Constant Extra Space needed)
        # Think about a way to use a concept from LL without actually converting 
        # nums array to a LL (fast and slow pointers)

        #Floyd's Algorithm
            # 1st while loop: 
                # slow = the value at that index 
                # fast = the next value at the next index 
                # when slow == fast, we break from the loop and move on to the 2nd
                # phase 
            
            # 2nd while loop: 
                # We keep one of the pointers(slow) at the intersection 
                # We create a new pointer that starts at the start of the array
                    # (finder pointer)
                # slow = the value at that index (where slow currently is)
                # finder = the value at that index (where finder currently is)

                # When slow == finder, return slow 

        #I: 
        fast, slow = 0, 0 
        
        #1st phase 
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast: 
                break 
        
        #2nd phase
        finder = 0
        while True: 
            finder = nums[finder]
            slow = nums[slow] 

            if slow == finder: 
                return slow 

        #R: 
        # nums = [1,2,3,2,2]
            #1st phase: 
                # slow = 1, fast = 2
                # slow = 2, fast = 2 

            #2nd phase: 
                # finder = 1, slow = 3
                # finder = 2, slow = 2, slow is returned (2)
        
        #E: Time: O(n), Space: O(1)
