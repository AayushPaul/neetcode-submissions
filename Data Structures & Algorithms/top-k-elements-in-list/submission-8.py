class Solution:
    # Time: 5:35 - 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #U: Return the k most freq elems in the nums array 
            # Get the frequency of each element with a hashmap 

        #M/P: Hashmap to get the frequency of each number 
            # Make the final array have the numbers with the k highest frequencies. 
        
        #I: 
        numFreq = {} 
        for i in range(len(nums)): 
            numFreq[nums[i]] = 1 + numFreq.get(nums[i], 0)
        
        key_val_arr = [] 

        for num, freq in numFreq.items(): 
            key_val_arr.append([num, freq])
        
        sortedArr = sorted(key_val_arr, key=lambda x: x[1])

        count = 0 
        finalArr = [] 
        while count < k: 
            subarray = sortedArr.pop() # pops key value pair subarray 
            finalArr.append(subarray[0]) #subarray = [2, 3]
            count += 1
        
        return finalArr 

        #R: 
        # nums = [1, 2, 2, 2, 3, 3], k = 2
            # One for loop goes through the nums array and determines the frequency of each number and creates a hashmap based on that 
            # hashmap = {1:1, 2:3, 3:2}
            
            # The next for loop goes through the keys and values of the hashmap and appends each (key, value) to the hashmap 
            # Sort the key, value pairs in the array based on the values/frequencies 

            # array = [(1, 1), (2, 3), (3, 2)], sorted array = [(1, 1), (3, 2), (2, 3)]
            # Initialize count variable to 0 
            # while count < k: 
                # pop key-value pairs from the sorted array AND add the corresponding keys to the final array 
                # Increase count 

            # Return the final array

            # sorted array = [(1, 1), (3, 2)] 
                # popped pair = (2, 3), key = 2
                # finalArr = [2]
                # count = 1

                # popped pair = (3, 2), key = 3
                # finalArr = [2, 3]
                # count = 2
            
            # finalArr = [2, 3]

        #E: Time: O(n + mlogm), Space: O(n) 
