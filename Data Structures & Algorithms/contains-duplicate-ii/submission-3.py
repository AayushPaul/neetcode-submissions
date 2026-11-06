class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #U: Return true if there are 2 distinct indices i and j such that the elements at those indices are duplicates 
        # in the size of the current window (k) 

        #M/P: Sliding Window 

        #I: 
        window = set() 
        i = 0 

        for j in range(len(nums)): 
            if abs(i - j) > k: 
                window.remove(nums[i])
                i += 1
            
            if nums[j] in window: 
                return True 

            window.add(nums[j])
            
        return False 

        #Time: O(n), #Space: O(min(n, k)) where n is the size of the array and k is the max distance between duplicates