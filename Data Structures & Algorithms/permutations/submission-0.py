class Solution:
    # Time: 4:34 - 
    def permute(self, nums: List[int]) -> List[List[int]]:
        #U: 

        #M/P: Recursion 

        #I: 
        if not nums: 
            return [[]]
        
        res = [] 
        perms = self.permute(nums[1:])  # nums = [2, 3]

        for p in perms: 
            for i in range(len(p) + 1):  
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy) 

        return res 
        
        #R: nums = [1, 2, 3]    # Rule: n! (ex: 3! = 6)
            # permute(nums[1:])
            # When the base case of null is reached, returns [[]]
            #  
            #  res = [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
            #                   perms/res = [[2, 3], [3, 2]]
            #                        perms/res = [[3]]
        
        #E: Time: O(n^2 * n!), Space: O(n * n!)