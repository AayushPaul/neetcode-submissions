class Solution:
    # Time: 12:21 - 12:40 
    def findDuplicate(self, nums: List[int]) -> int:
        #U: Find the duplicate number 

        #M/P: Hashmap to keep track of the frequency of each number
            # Return the number whose frequency > 1 

            # Build the hashmap by looping through the nums array once 
            # Iterate through the hashmap's key-value pairs using the Python items method 

            # If value > 1, return the corresponding key

        #I: 
        freqMap = {} 
        for num in nums: 
            if num in freqMap: 
                freqMap[num] += 1
            else: 
                freqMap[num] = 1
        
        for num, count in freqMap.items(): 
            if count > 1: 
                return num

        #R: nums = [1, 2, 3, 2, 2]
            # hashmap = {1:1, 2:3, 3:1}

            # 2 is returned (duplicate)

        #E: Time: O(n), Space: O(n)