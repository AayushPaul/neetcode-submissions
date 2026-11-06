class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #U: Given the nums array and the target, 
        #we have to return the indices i and j such that 
        #nums[i] + nums[j] == target 

        #M: hashmap, for loop to go through nums array

        #P: 
            #1. Initialize a new hashmap 
            #2. For loop to go through nums array
            #3.     diff = target - nums[i]
            #4.     j is the index of the difference(hashmap[diff])
            #5.     if diff in hashmap, we return [i, hashmap[diff]]
        
        #I: 
        hashmap = {}
        for i in range(len(nums)): 
            diff = target - nums[i]

            if diff in hashmap: 
                return [hashmap[diff], i]
            
            hashmap[nums[i]] = i
        
        #R: 
            #Go through example 2
        
        #E: Time: O(n), Space: O(n)
