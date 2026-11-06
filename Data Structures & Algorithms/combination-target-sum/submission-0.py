class Solution:
    # Time: 6:45 - 7:41
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #U: Return a list of all unique combinations of nums where chosen numbers sum to target. 
            # The same number may be chosen from nums an unlimited number of times. 

        #M/P: Backtracking

        #I: 
        result = [] 
        nums.sort() 

        def backtracking(start, comb, combSum): 
            if combSum == target: 
                result.append(comb.copy())
                return 

            for i in range(start, len(nums)): 
                if combSum + nums[i] > target: 
                    break 

                comb.append(nums[i])
                backtracking(i, comb, combSum + nums[i])
                comb.pop() 

        backtracking(0, [], 0)
        return result 

        #R: nums = [2, 5, 6, 9]
            # output: []
            # curr comb = [2, 2, 5], combSum = 10