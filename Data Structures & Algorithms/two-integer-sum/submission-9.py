class Solution:
    #Time: 6:25 - 6:42
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #U: Given nums array and target, return indices i and j st nums[i] + nums[j] == target 
        # and i != j 

        # Return answer with smaller index first 

        #M/P: Hashmap (more challenging)
        # Keys are actual values, values are indices (switched up) 
            #Iterate through nums array with for loop 
            
        #I: 
        stored = {} # Stores indices and corresponding values from nums array 

        for i in range(len(nums)): 
            diff = target - nums[i]

            if diff in stored: 
                return [stored[diff], i] 

            stored[nums[i]] = i
        
        #R: nums = [4,5,6], target = 10
            # stored = {4:0, 5:1, }
            # returns [0, 2]
        
        #E: Time: O(n), Space: O(n)
        


