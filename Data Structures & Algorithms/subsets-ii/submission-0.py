class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #U: 
        curSet, subsets = [], [] 
        nums.sort() 

        def backtrack(i): 
            if i == len(nums): 
                subsets.append(curSet.copy())
                return 
            
            # Decide to append nums[i]
            curSet.append(nums[i])
            backtrack(i + 1) 
            curSet.pop()  

            # Decide NOT to append nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]: 
                i += 1
            backtrack(i + 1)

        backtrack(0) 
        return subsets

        #E: Time: O(n * 2^n), Space: O(n * 2^n) 