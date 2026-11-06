class Solution:
    # 12:49 - 
    def combine(self, n: int, k: int) -> List[List[int]]:
        #U: Return all possible combinations of k numbers from the range [1, n]

        #M/P: Backtracking 

        #I:
        res = [] 
        comb = [] 

        def backtrack(i, comb): 
            if len(comb) == k: 
                res.append(comb.copy())
                return 
            
            if i > n: 
                return 

            # Decision to append elem
            comb.append(i) 
            backtrack(i + 1, comb) 
            comb.pop() 

            # Decision to not append elem 
            backtrack(i + 1, comb)

        backtrack(1, comb)
        return res 

        #R: n = 3, k = 2
            # res = [[1, 2], [1, 3], [2, 3]]
            # comb = []
