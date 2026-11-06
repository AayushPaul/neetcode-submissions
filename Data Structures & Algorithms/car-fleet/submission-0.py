class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #U: We are given 2 arrays of integers (position and speed), both of length n. 
            #position[i] = position of ith car (mi) 
            # speed[i] = speed of ith car (mph) 
        # A car fleet is non-empty set of cars driving at the same position 
        # and same speed; single car is also considered a car fleet. 

        #M/P: 
        # Keep track of the times of each car in the stack. 

        # Use the zip function to get the positions and speeds and add them 
        # via list comprehension or add to a new list 

        # Reverse the positions and speeds to check if previous car catches up with 
        # new car (<= time of new car in stack)
            # If so, pop the most recent time off the stack. 
        
        # Return length of stack == # car fleets 

        #I: 
        posSpeeds = [(p, s) for p, s in zip(position, speed)]
        posSpeeds.sort(reverse=True)
        stack = []

        for (p, s) in posSpeeds: 
            # Appends the times of each car (time to reach the target)
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop() 
        
        return len(stack)

        #E: Time - O(n), Space - O(n)