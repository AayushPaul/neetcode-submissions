class Solution:
    #Time: 12:08 - 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       #U: Return indices i and j st nums[i] + nums[j] == target
       # and i != j; return answer with smaller index first 

        #M/P: 
            # Use hashmap to keep track of the encountered keys/nums 

        #I: 
        hashmap = {}
        for i in range(len(nums)): 
            diff = target - nums[i]
            if diff in hashmap: 
                return [hashmap[diff], i]

            hashmap[nums[i]] = i
        
        #R: [4, 5, 6], target: 10
            # hashmap = {4: 0, 5: 1, 6: }
            # return [0, 2] 
        
        #E: Time: O(n), Space: O(n) 