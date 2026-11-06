class Solution:
    # Time: 10:37 - 
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # U: Given list of points 
        # Return k closest points to the origin (0, 0) 

        # M/P: Determine the distance between each point from the origin with a for loop using the Euclidean distance
        # formula. 
            # Add distance with corresponding points to array 
            # Heapify that array (min-heap) 

            # Initialize a count variable and res array 
            # While loop (count < k) 
                # Keep popping points from the heap and keep adding them to the res array
                    # heapq.heappop(minHeap)    # Returns the min element from the heap (returns the current closest point)
                    # count += 1

        # Based on the distances, use a min heap to store the closest points. So, the point with the least distance
        # is basically the root of the min heap. 

        #I: 
        minHeap = [] 
        for x, y in points: 
            dist = math.sqrt((x**2) + (y**2))
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap) 
        count, res = 0, [] 

        while count < k: 
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])    #Ex: [0, 2], [2, 0]
            count += 1
        
        return res 

        #R: [[0, 2], [2, 0], [2, 2]], k = 2 
        # minHeap = [[2, 0, 2], [2, 2, 0], [2.82, 2, 2]]    #Already heapified

        #E: Time: O(n + klogn), Space: O(n) 