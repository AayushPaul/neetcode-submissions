class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #U: Given nums array, return all the triplets [nums[i], nums[j], nums[k]] where the sum of the 
        # 3 elems = 0 

        #M/P: 
            # Start with the brute force approach 

        #I: 
        res = []

        for i in range(len(nums)): 
            for j in range(i + 1, len(nums)): 
                for k in range(j + 1, len(nums)): 
                    curSum = nums[i] + nums[j] + nums[k]
                    sortedArr = sorted([nums[i], nums[j], nums[k]])

                    if curSum == 0 and sortedArr not in res: 
                        res.append(sortedArr)

        return res

        #E: Time: O(n^3), Space: O(m)