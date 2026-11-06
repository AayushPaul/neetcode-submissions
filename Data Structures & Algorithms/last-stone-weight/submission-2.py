class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Sorting the stones using heapify function 
        stones = [-s for s in stones]
        heapq.heapify(stones)

        #While loop will continue until there is no more than one stone remaining
        while len(stones) > 1: 
            x = heapq.heappop(stones) #Left stone in tree
            y = heapq.heappop(stones) #Right stone in tree 

            if x < y: 
                x = x - y
                heapq.heappush(stones, x)
        
        #After while loop ends, the remaining stone is added to the heap(stones)
        stones.append(0)
        return abs(stones[0]) #Accounts for the edge case where the difference between y and x is negative