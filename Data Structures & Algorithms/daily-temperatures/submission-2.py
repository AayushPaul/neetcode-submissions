class Solution:
    #Time: 5:52 - 6:22 
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #U: Return an array result where result[i] is the # days after the ith day when a warmer temp appears 

        #M/P: Brute force approach (two nested for loops)
            # Cons: higher time complexity 

            # Stack approach 
        #I: 
        result = [0] * len(temperatures) 
        stack = [] 

        for i, temp in enumerate(temperatures): 
            while stack and temp > stack[-1][1]: 
                stackIndex, stackTemp = stack.pop() 
                result[stackIndex] = i - stackIndex 
            
            stack.append((i, temp))
        
        return result

        #R: 
            # Example 1: temps = [30,38,30,36,35,40,28]
                # stack = [(5, 40), (6, 28)]  # For previous indices, pop previous pairs with stack.pop(0) 
                # Output/result: [1,4,1,2,1,0,0] 
        
        #E: Time: O(n), Space: O(n)
