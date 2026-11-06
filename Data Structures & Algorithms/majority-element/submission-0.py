class Solution:
    # Time: 11:47 - 12:08
    def majorityElement(self, nums: List[int]) -> int:
        #U: Return majority element (element that appears more than 
        # floor(n/2) times)

        #M/P:
            # Store frequency of numbers using hashmap 
            # Iterate through the values of each number/key in the hashmap
            
            # Return the number/key whose value > floor(n/2)
                # This is the majority element 

        #I:  
        minTimes = len(nums) // 2  # Like floor division 
        frequencyMap = {} 

        for num in nums: 
            if num not in frequencyMap: 
                frequencyMap[num] = 1
            else: 
                frequencyMap[num] += 1
        
        # key = actual number, value = frequency of that number in nums array
        for key, value in frequencyMap.items(): 
            if value > minTimes: 
                return key

        #R: Example 1
            # frequencyMap = {5: 4, 1: 3}, output: 5
        
        #E: Time: O(n), Space: O(n) 