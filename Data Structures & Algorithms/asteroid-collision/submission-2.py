class Solution:
    #Time: 11:26 - 12:02 
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #U: If two asteroids meet, the smaller one will explode (absolute value of the asteroids)
            # If both are the same size, both will explode. 
            # Two asteroids moving in the same direction will never meet. 
        
        #M/P: Iterate through the asteroids array with for loop 

        #I: 
        stack = [] 

        for i in range(len(asteroids)): 
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                if abs(stack[-1]) < abs(asteroids[i]): 
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(asteroids[i]): 
                    stack.pop()
                break
            else:
                stack.append(asteroids[i])
        
        return stack

        #E: Time: O(n), Space: O(n)