class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
       #U: stones[i] represents weight of the ith stone 
        #  We choose the two heaviest stones with weight x and y and smash them together 
            # If x == y, both stones are destroyed 
            # If x < y, weight x is destroyed and weight y = y - x

            # Continue sim until there is <= 1 stone 

            # Return weight of last remaining stone OR return 0 if none remain. 

        #M/P: Min Heap (The two largest stones should be the two smallest stones because those will be eliminated first)
            # Turn all the stone weights into negative nums
            # Heapify this new array of negative nums 
            # x = left/first stone, y = right/second stone 

            # While len(heap) > 1: 
                # Note: comparing the values of stone x and stone y in the heap 
                # If x == y, both stones are destroyed or popped from the heap 
                # If x < y, x is popped/destroyed, but y = y - x

            # Two possible end cases: One stone remaining (one popped at the end - x < y), 
            # 0 stones remaining (both popped at the end)

        #I: 
        for i in range(len(stones)): 
            stones[i] = -(stones[i])    # Changes all nums to negative 
        
        heapq.heapify(stones) # stones is a heap now 

        # On each iteration, after one or two stones is popped, the min element becomes the root and parent < children
        # because of heap property (stones is already heapified) 
        while len(stones) > 1: 
            #Note: The heaviest stones are popped at first no matter what. 
            x = heapq.heappop(stones) #heappop pops the smallest element and returns it while preserving the min heap structure.
            y = heapq.heappop(stones) 
            
            if x < y: 
                x = x - y
                heapq.heappush(stones, x) #heappush inserts a new item into a regular list while maintaining the min-heap property.
            
        if len(stones) == 1: 
            return abs(stones[0])
        else: 
            return 0    #No stones remain

        #R: 
            #   2                -6
            #  / \               / \
            # 3   6     ->     -4  -2
            #/\                /\
         #  2  4              -3 -2
        
        #E: Time: O(n), Space: O(n) 