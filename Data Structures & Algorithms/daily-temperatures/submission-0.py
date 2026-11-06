class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) #initially filled with zeroes
        stack = [] #temp, index 
        
        #Create for-each loop in python with enumerate method 
        for i, t in enumerate(temperatures): 
            while stack and t > stack[-1][0]: 
                stackTemp, stackIndex = stack.pop() 
                result[stackIndex] = i - stackIndex

            stack.append((t, i))
        
        return result 
