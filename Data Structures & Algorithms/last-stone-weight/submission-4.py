class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
       # Time: 12:56 - 
       # We choose the 2 heaviest stones at each step with weight x and y and smash
       # them together 

       # If x == y, both are destroyed 
       # If x < y, stone of weight x is destroyed and stone of weight y has 
       # new weight y - x. 

       # Continue simulation until there is at most 1 stone remaining 
       # Return weight of last stone or return 0 if none remain. 

       #M/P: Heaps 
       # Make all the values negative. 
       # Heapify the stones array 
       # While len(heap) > 1: 
         # Pop the 2 min elements from the heap 
         # If the values of both elements are the same, no new value is added
         # to the heap 
         # If the values are different, then append the value (y - x) to the heap 
        
        # If len(heap) == 1, return the only value; convert the value from (-) to (+)
        # If len(heap) == 0, return 0 

        #I: 
        #Time: O(n) 
        for i in range(len(stones)): 
            stones[i] = -stones[i]
        
        heapq.heapify(stones)   #Officially creates a minHeap 

        while len(stones) > 1: 
            x = heapq.heappop(stones) #smaller element
            y = heapq.heappop(stones) #larger element

            if x < y: 
                newVal = x - y
                heapq.heappush(stones, newVal)
        
        if len(stones) == 1: 
            return abs(stones[0])
        else: 
            return 0 

        #E: Time: O(nlogn) , Space: O(n)