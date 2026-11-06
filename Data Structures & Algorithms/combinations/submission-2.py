class Solution:
    # 5:52 - 6:17 
    def combine(self, n: int, k: int) -> List[List[int]]:
        #U: Return all possible combinations of k numbers chosen from the range [1, n]

        #M/P: Backtracking 
        # Keep track of current combinations with a separate array
        # When length of current combination array == k, add it to result array 
        # Return and then pop elements 

        #I: 
        res = [] 

        def backtrack(start, comb): 
            if len(comb) == k: 
                res.append(comb.copy())
                return 
            
            for i in range(start, n + 1): 
                comb.append(i) 
                backtrack(i + 1, comb)
                comb.pop() 

        backtrack(1, [])
        return res

       #R: n = 3, k = 2
        # res = [[1, 2], [1, 3], [2, 3]] 
        # comb = []

        # Tree format: 
            #       1   2
            #      / \   \
            #     2   3   3
        
        #E: Time: O(k * C(n, k)), Space: O(k * C(n, k))