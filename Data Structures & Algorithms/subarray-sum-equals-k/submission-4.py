class Solution:
    # Time: 4:30 - 5:17
    def subarraySum(self, nums: List[int], k: int) -> int:
        #U: Return the total # subarrays whose sum equals to k. 

        #M/P: 
            
        #I: 
        res = 0
        curSum = 0 
        prefixSums = {0 : 1}

        for num in nums: 
            curSum += num 
            diff = curSum - k 

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        
        return res 

        #R: 
            #Ex 1: nums = [2, -1, 1, 2], k = 2
        
        #E: Time: O(n), Space: O(n) 