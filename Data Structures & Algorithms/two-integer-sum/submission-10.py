class Solution:
    #Time: 4:55 - 5:20
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #U: Given nums array and target, return indices i and j st nums[i] + nums[j] == target 
        # and i != j 

        # Return answer or array with smaller index first 

        #M/P: Hashmap (key should be the actual element, value should be the index)

        #I: 
        elemIndices = {} # key: actual element, value: index of that element 
        for i in range(len(nums)): 
            difference = target - nums[i]
            if difference in elemIndices: 
                return [elemIndices[difference], i]

            elemIndices[nums[i]] = i  

        #R: 
        # nums = [3, 4, 5, 6], target = 7 
        # elemIndices = {3:0, }
        # ans = [0, 1]

        #E: Time: O(n), Space: O(n) 