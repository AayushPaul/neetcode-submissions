class Solution:
    # Time: 10:30 -  
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #U: position[i]: position of the ith car (mi) 
            # speed[i]: speed of the ith car (mph) 

            # destination: at position target miles 
            
            #Note: As long as previous car's time is <= current car's time, they are in the same fleet

            # To get the time a car reaches the destination: time = (target - pos) / speed  

        #M/P: 
            # Python zip function, stack that stores the times of the cars 
            # Whenever a previous car's time <= current car's time, pop the topmost time from the stack 
            # Return len(stack) at the end 

        #R: target = 10, position = [4, 1, 0, 7], speed = [2, 2, 1, 1]
            # cars = sortedArr = [0, 1, 4, 7], speed = [1, 2, 2, 1]
            # reversedSortedArr = [7, 4, 1, 0], speed = [1, 2, 2, 1]
            # 1st iteration: time = (10 - 7) // 1 = 3
                # Append time to the stack: stack = [3]
            # 2nd iteration: time = (10 - 4) // 2 = 3 
                # Append time to the stack: stack = [3]
                # Since len(stack) >= 2 && stack[-1] <= stack[-2], pop the <= time from the stack 
            
            # 3rd iteration: time = (10 - 1) // 2 = 4 
                # stack = [3, 4]
            
            # 4th iteration: time = (10 - 0) // 1 = 10 
                # stack = [3, 4, 10]
            
                #len(stack) = 3 
        
        #I: 
        stack = [] 
        posSpeeds = list(zip(position, speed))
        sorted_pos_speeds = sorted(posSpeeds, reverse=True)

        for pos, speed in sorted_pos_speeds: 
            time = (target - pos) / speed 
            stack.append(time) 

            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop() 

        return len(stack)   # car fleets

        #E: Time: O(nlogn), Space: O(n) 