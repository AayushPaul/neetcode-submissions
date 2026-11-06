class Solution:
    #Time: 3:08 - 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       #U: Given nums and target, return indices i and j st 
       # nums[i] + nums[j] == target, i != j

       #M/P: Use hashmap to keep track of keys(actual elems) and values(indices)

       #I: 
       stored = {}

       for i in range(len(nums)): 
        diff = target - nums[i]
        
        if diff in stored: 
            return [stored[diff], i] 

        stored[nums[i]] = i
    
    #E: Time: O(n), Space: O(n) 