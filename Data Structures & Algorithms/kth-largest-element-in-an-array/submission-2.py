class Solution:
    # Time: 10:28 - 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #U: Return kth largest element in the array 

        #M/P: Max Heap (largest element will be the root in the heap)

        #I: 
        heapq.heapify_max(nums) # O(n) 

        while k > 1:
            heapq.heappop_max(nums) # Pops the root, which is the current largest number 
            k -= 1

        return nums[0]

        #R: [2, 3, 1, 5, 4], k = 1
        #  ans: 4 (nums[0])

        #E: Time: O(n + klogn), Space: O(1)