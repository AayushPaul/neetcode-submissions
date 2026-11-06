class NumArray:
    # Time: 1:00 - 
    #M/P: Prefix Sum approach 
    def __init__(self, nums: List[int]):
        self.prefix = [] 
        total = 0 

        for num in nums: 
            total += num
            self.prefix.append(total) 

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0
        finalSum = rightSum - leftSum 
        return finalSum 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

#R: [-2, 0, 3, -5, 2, -1]
    # prefix = [-2, -2, 1, -4, -2, -3]
    # left, right = 2, 5
    # sum of subarray using nums array = 3 + (-5) + 2 + (-1) = -1 
    # sum of subarray using prefix array = prefix[right] - prefix[left - 1] = -3 - (-2) = -1 

#E: Time: O(n), Space: O(n) 