class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #U: Return median value among all the elements of the 2 arrays 

        #M/P: Perform binary search on both arrays 

        #I: 
        A, B = nums1, nums2 
        total = len(nums1) + len(nums2)
        half = total // 2

        # A will always be the shorter array 
        if len(B) < len(A): 
            A, B = B, A 
        
        left, right = 0, len(A) - 1

        while True: 
            APart = (left + right) // 2 # The last index in the half partition in the smaller array (A) 
            BPart = half - APart - 2 # The last index in the half partition in the larger array (B) 

            Aleft = A[APart] if APart >= 0 else float("-infinity")
            Aright = A[APart + 1] if (APart + 1) < len(A) else float("infinity")
            Bleft = B[BPart] if BPart >= 0 else float("-infinity")
            Bright = B[BPart + 1] if (BPart + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Aright >= Bleft: 
                if total % 2 != 0: 
                    return min(Aright, Bright)
                
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright: 
                right = APart - 1
            else: 
                left = APart + 1


        #Time: O(log(m + n)), #Space: O(1)