class Solution:
    # Time: 11:40 - 12:05 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #U: Given nums array, return all possible subsets of nums. 

        #M/P: 

        #I: 
        subsets, curSet = [], [] 

        def dfs(i): 
            if i >= len(nums): 
                subsets.append(curSet.copy())
                return 
            
            # Decision to include nums[i]
            curSet.append(nums[i]) 
            dfs(i + 1) 
            curSet.pop() 

            # Decision to NOT include nums[i]
            dfs(i + 1) 
        
        dfs(0) 
        return subsets

        #R: 
            # nums = [1, 2, 3]
            #      / \
            #     1   []
            #    / \  / \
            #   1,2 1
            #   /  \
            # 1,2,3 1,2