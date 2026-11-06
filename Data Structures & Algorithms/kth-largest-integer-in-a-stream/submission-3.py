class KthLargest:

    def __init__(self, k: int, nums: List[int]): 
        self.k = k 
        self.heap = nums 

        heapq.heapify(self.heap) # Transforms the list into a min-heap 

        while len(self.heap) > self.k: 
            heapq.heappop(self.heap)
        
    def add(self, val: int) -> int: 
        #U: Adds integer val to the stream and returns kth largest integer in stream 

        #M/P:  

        #I: 
        heapq.heappush(self.heap, val) 
        
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Returning the value of the kth largest element (the root of the min-heap)
        return self.heap[0]