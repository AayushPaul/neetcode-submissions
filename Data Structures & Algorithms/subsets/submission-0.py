class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #U: Given array nums of unique integers, return all possible subsets of nums. 

        #M/P: 

        #I: 
        res = [] 
        subset = [] 

        def dfs(i): 
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)
            subset.pop() 
            dfs(i + 1) 

        dfs(0) 
        return res
        
        #R: 
            # nums = [1, 2, 3]
            # subset = [] 
            # res = []

            #       1
            #      / \
            #     1   2
            #    /
            #   
        
        #E: Time: O(n * 2^n), Space: O(n)