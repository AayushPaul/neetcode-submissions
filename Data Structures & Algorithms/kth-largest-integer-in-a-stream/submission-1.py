class KthLargest:

    def __init__(self, k: int, nums: List[int]): 
        self.k = k 
        self.minHeap = nums 

        heapq.heapify(self.minHeap)
                                        #     1
                                        #    / \
                                        #  2     3
        
        while len(self.minHeap) > self.k: 
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int: 
        #U: This method adds the integer val to the stream and returns 
        # the kth largest integer in the stream(k is in the constructor)

        #M/P: Heaps 
            # In the constructor, I am going to heapify the nums array(minHeap) 
            # Add new value to the heap using heappush 
            # If length of the heap > k: 
                # Pop the minimum element from the heap 
            
            # Return self.minHeap[0]

        #I: 
        heapq.heappush(self.minHeap, val)   
        if len(self.minHeap) > self.k: 
            heapq.heappop(self.minHeap) # Takes O(logn)

        return self.minHeap[0]  #constant time 
        
    #E: Time: O(m * logn), Space: O(n)