class Solution:
    # Time: 12:10 - 
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #U: Numbers is sorted in increasing order. 
            # Return the indices (1-indexed) of 2 nums [index1, index2] where numbers[index1] + 
            # numbers[index2] = target and index1 < index2; index1 != index2

            # O(1) additional space 

        #M/P: Two Pointers 
            # left = 0, right = len(numbers) - 1
            # While loop 
                # if value at left + value at right > target, right pointer moves to the left 
                # if value at left + value at right < target, left pointer moves to the right 
                # If the sum of the values = target, return [left + 1, right + 1]
        
        #I: 
        left, right = 0, len(numbers) - 1

        while left < right: 
            if numbers[left] + numbers[right] > target: 
                right -= 1
            elif numbers[left] + numbers[right] < target: 
                left += 1
            else: 
                return [left + 1, right + 1]

        #R: numbers = [1, 2, 4, 5, 6], target = 5
            # l = 0, r = 2 
            # return [l + 1, r + 1]