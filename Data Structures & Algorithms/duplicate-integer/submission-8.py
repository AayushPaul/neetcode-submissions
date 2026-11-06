class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #U: Given nums, return true if any value appears more than once
        # Else, return false 

        #M/P: Hashset, go through nums with for loop and each num to hashset
            # If num already exists in hashset, return true 
        
        #I: 
        numsSet = set() 

        for num in nums: 
            if num in numsSet: 
                return True 

            numsSet.add(num) 
        
        return False

        #E: Time: O(n), Space: O(n) 