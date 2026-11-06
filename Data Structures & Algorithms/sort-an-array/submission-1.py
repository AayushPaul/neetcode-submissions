class Solution:
    # Time: 12:45 - 1:27 (subtract 7 min)
    def sortArray(self, nums: List[int]) -> List[int]:
        #U: Sort the array in ascending order and return it without sorting the array with a built-in function
        # Smallest space complexity 

        #M/P: Bruter force nested for loop approach using Python min function on each outer loop iteration 

        #I: 
        for i in range(len(nums)): 
            for j in range(i + 1, len(nums)): 
                minNum, temp = nums[i], nums[i]

                if nums[j] < minNum: 
                    minNum = min(minNum, nums[j]) 
                    nums[i] = minNum 
                    nums[j] = temp

        return nums

        #R: nums = [10, 9, 1, 1, 1, 2, 3, 1]
        # output = [1, 9, 1, 1, 1, 2, 3, 10] #2nd outer loop iteration 
        # output = [1, 1, 1, 1, 9, 2, 3, 10] #3rd outer loop iteration 
        # output = [1, 1, 1, 1, 9, 2, 3, 10] #4th outer loop iteration 
        # output = [1, 1, 1, 1, 2, 9, 3, 10] #5th iteration 
        # output = [1, 1, 1, 1, 2, 3, 9, 10] #6th iteration 

        #E: Time: O(n^2), Space: O(1)