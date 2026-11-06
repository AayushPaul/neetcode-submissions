class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Time: 11:08 - 
        
        #U: Return the kth largest element in the sorted array 

        #M/P: Heaps 
            # Heapify the nums array; convert the nums array into a min heap 
            # While len(nums) > k: 
                # Pop the min elements from the heap 
            
            # Return the first element in the heap; this is the kth largest element 
        
        #I: 
        # Time: O(n)
        heapq.heapify(nums) #Converting the nums array into a min heap 

        while len(nums) > k: 
            heapq.heappop(nums) # Time: O(logn)
        
        return nums[0]

        #R: 
        # Ex 2: nums = [2, 3, 1, 1, 5, 5, 4] -> heap version: [4, 5, 5], k = 3, returns 4 
        
        # Ex 3: nums = [2, 1], k = 2 -> heap version: [1, 2], returns 1

        # Ex 1: nums = [1], k = 1 -> heap version: [1], returns 1

        #E: Time: O(nlogn), Space: O(n)