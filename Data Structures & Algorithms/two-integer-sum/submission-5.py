class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #U: Return indices i and j such that nums[i] + nums[j] == target. 
        #Return answer with smaller index first.       
        hashmap = {}

        for i , n in enumerate(nums): 
            diff = target - n
            
            if diff in hashmap: 
                return [hashmap[diff], i]
                
            hashmap[n] = i
