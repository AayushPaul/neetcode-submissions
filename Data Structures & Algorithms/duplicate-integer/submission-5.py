class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #U: Given an array nums, return true if any value appears 
        #more than once in the nums array 

        #M: hashset of nums, for loop to go through the nums array, 
        # conditional to check if a number is already in the set

        #P: 
            #Create hashset 
            #for each number in nums: 
                #Add number to the hashset
                # If number if already in the hashset, return true 
            
            #return false 
        
        #I: 
        hashset = set()

        for num in nums: 
            if num in hashset: 
                return True 
                
            hashset.add(num)
        
        return False 

        #R: 
            #nums = [1, 2, 3, 3] 
        
        #E: Time: O(n), Space: O(n)
