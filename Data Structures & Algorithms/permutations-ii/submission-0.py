class Solution:
    # Time: 11:18 - 12:00
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #U: Nums might contain duplicates; return all possible unique permutations in any order. 

        #M/P: Hashset and Recursion
            # Count the frequency of each number 
            # Use the same recursion approach. However, check if permutation is already in the hashset. 
            # If NOT, then add it to the list of permutations in the level. 

        #I: 
        hashset = set() 
        res = [] 

        if not nums: 
            return [[]]

        perms = self.permuteUnique(nums[1:])
        for p in perms: 
            for i in range(len(p) + 1): 
                p_copy = p.copy() 
                p_copy.insert(i, nums[0])
                tuple_p_copy = tuple(p_copy)

                if tuple_p_copy not in hashset: 
                    res.append(p_copy)
                    hashset.add(tuple_p_copy)
        
        return res

        #R: 
            # nums = [1, 1, 2]
            # hashset = ([1, 1, 2], [1, 2, 1], [2, 1, 1])

            #  [[1, 1, 2], [1, 2, 1], [2, 1, 1]] <- final answer 
                #  [[1, 2], [2, 1]]
                #       [[2]]