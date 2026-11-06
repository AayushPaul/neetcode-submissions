class Solution:
    #Time: 5:52 - 
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #U: Return an array result where result[i] is the # days after the ith day when a warmer temp appears 

        #M/P: Brute force approach (two nested for loops)
            # Cons: higher time complexity 

        #I: 
        result = [0] * len(temperatures) 

        for i in range(len(temperatures)): 
            for j in range(i + 1, len(temperatures)): 
                if temperatures[j] > temperatures[i]: 
                    numDays = j - i 
                    result[i] = numDays 
                    break 

        return result 

        #R: 
            # Example 1: temps = [30,38,30,36,35,40,28]
                # Output: [1, 4, 1, 2, 1, 0, 0]
        
        #E: Time: O(n^2), Space: O(1)
