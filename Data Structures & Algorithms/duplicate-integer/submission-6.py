class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #U: Return true if any value appears more than once in the array; 
        # return false 

        #M/P: 
            # Initialize hashset

            # Iterate through the nums array with for each loop 
                # If number is in the hashset, return True(found duplicate)
                # Add number to the hashset 

        #I: 
        hashset = set() 

        for num in nums: 
            if num in hashset: 
                return True 

            hashset.add(num)
        
        return False 

        #E: Time: O(n), Space: O(n)