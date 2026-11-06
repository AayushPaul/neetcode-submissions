class Solution:
    def findMin(self, nums: List[int]) -> int:
        #U: nums is rotated and sorted 
        # Return the min element of this array in O(logn) time 

        # M/P: Binary Search 

            # l, r = 0, len(nums) - 1
            # startingMid = (l + r) // 2
            # minVal = nums[startingMid]

            # while l <= r: 
                    # mid = (l + r) // 2
                    # minVal = min(minVal, nums[mid])

                    # if nums[mid] > nums[r]: 
                        # l = mid + 1
                    # else: 
                        # r = mid - 1
        
            # return mid 

        #I:   
        l, r = 0, len(nums) - 1
        startingMid = (l + r) // 2
        minVal = nums[startingMid]

        while l <= r: 
            mid = (l + r) // 2
            minVal = min(minVal, nums[mid])

            if nums[mid] > nums[r]: 
                l = mid + 1
            else: 
                r = mid - 1
        
        return minVal

        #R: 
            # nums = [3, 4, 5, 6, 1, 2] # rotated between 1 and 6 times, the actual number was 4 times 
                # l, r = 0, 5 
                # startingMid = 2
                # minVal = 5

                # Enter while loop 
                    # 1st iteration 
                        # mid = 2 
                        # minVal = min(5, 5) = 5
                        # left is at 3 now, r is at 5 

                    # 2nd iteration 
                        # mid = 4 
                        # minVal = min(5, nums[mid]) = min(5, 1) = 1
                        # right is at 3, left is at 3 

                    # 3rd iteration 
                        # mid = 3
                        # minVal = min(1, nums[mid]) = min(1, 6) = 1
                        # left at 4, right at 3 (l > r and program exits while loop) 
                
                # min val is returned 

        #E: Time: O(logn), Space: O(1)