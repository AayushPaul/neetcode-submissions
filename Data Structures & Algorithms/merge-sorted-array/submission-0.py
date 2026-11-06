class Solution:
    # Time: 1:20 - 1:57 
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #U: 
            #m = # valid elems in nums1
            #n = # elems in nums2

            # Both nums1 and nums2 are sorted in increasing order. 

        #M/P: Two Pointer Method (pointer for each array) 
            # while loop
                # Compare the elems at the pointers
        
        #I: 
        l, r = 0, 0 
        res = [] 

        while l < m and r < n: 
            if nums1[l] > nums2[r]: 
                res.append(nums2[r])
                r += 1
            else: 
                res.append(nums1[l])
                l += 1
            
        res.extend(nums1[l:m])
        res.extend(nums2[r:n])
        
        nums1[:] = res