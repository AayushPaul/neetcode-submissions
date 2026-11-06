class Solution:
    #Time: 12:48 - 1:05 AM 
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #U: Return the minimal length of subarray whose sum is >= target. If there is no such subarray, return 0. 

        #M: Sliding Window 

        #P: 
            # left = 0 
            # total variable 
            # length = positive infinity, not really a finite number 

            # for loop that increments the right pointer 
                # while loop (condition is total >= target)
                    # Use the min function to find the curr min length: min(length, right - left + 1)
                    # total -= nums[left]
                    # left += 1
                
            # If length is positive infinity, return 0. If the length is something else, that means there is a valid subarray, so we can 
            # return the actual length  

        #I: 
        left, total = 0, 0 
        length = float("inf") #Positive Infinity 

        for right in range(len(nums)): 
            total += nums[right]

            while total >= target: 
                length = min(length, right - left + 1)
                total -= nums[left]
                left += 1
            
        return 0 if length == float("inf") else length

        #E: Time: O(n), Space: O(1)