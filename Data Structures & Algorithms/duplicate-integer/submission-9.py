class Solution:
    #Time: 12:38 - 12:43
    def hasDuplicate(self, nums: List[int]) -> bool:
        #U: Given nums, return true if any value appears more than once
        # Else, return false 

        #M/P: hashset 
            # Iterate through the nums array with a for loop 
            # Add each number to the hashset 

            # If current number encountered is in the hashset, there is a duplicate 
                # Return true     

        #I: 
        hashset = set() 
        for num in nums: 
            if num in hashset: 
                return True 

            hashset.add(num) 
        
        return False

        #E: Time: O(n), Space: O(n) 