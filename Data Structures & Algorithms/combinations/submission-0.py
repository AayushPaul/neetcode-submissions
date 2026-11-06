class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #U: Given 2 integers n and k, return all possible combinations of k numbers chosen from range [1, n]

        #M/P: 
        # initialize a combs array that keeps track of the different combinations 
        # Have a separate function that keeps track of the current combinations of length k only 
        
        # In the helper function: 
            # if the current combination has length k, copy the current combination to the combs array and return. 
            # If the current index (i) of the helper function > n, return. 
        
            # Have a for loop that goes from i to n + 1
            # Helper function recursive call 
            # Pops elements each time function is returned 
        
        # In the main function, call helper function 

        #I: 
        combs = [] 
        self.helperFunc(1, [], combs, n, k)
        return combs 

    def helperFunc(self, i, currComb, combs, n, k): 
        if len(currComb) == k: 
            combs.append(currComb.copy())
            return 
        
        if i > n: 
            return 
        
        for j in range(i, n + 1): 
            currComb.append(j) 
            self.helperFunc(j + 1, currComb, combs, n, k)
            currComb.pop() 

        #R: n = 3, k = 2
            # combs = [[1, 2], [1, 3], [2, 3]]
            # currComb = []