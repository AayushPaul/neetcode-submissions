class Solution:
    # Time: 11:18 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #U: Return the k most freq elems in the nums array 

        #M/P: Hashmap 
            # First step is creating the hashmap 

            # For each loop that goes through the key-value pairs (.items) in Python 
                    # Add each pair to an array [value, key]
                
            # Sort the array of pairs 

            # Initialize counter 
            # Pop the pairs from the array while count != k 
                # On each iteration, increment count and pop the pairs 
                # Add the 2nd element from each pair to the final result array (2nd elem = elem in nums array)
            
            # Return final array

        #I: 
        freqMap = {} 
        for num in nums: 
            if num not in freqMap: 
                freqMap[num] = 1
            else: 
                freqMap[num] += 1

        array = [] 
        for num, freq in freqMap.items(): 
            array.append([freq, num])
        
        sortedArr = sorted(array) 

        count = 0
        res = [] 
        while count != k: 
            pair = sortedArr.pop() #[4,3] is popped 
            res.append(pair[1])
            count += 1
        
        return res

        #R: 
            # nums = [1, 3, 3, 3, 3, 2, 2, 2], k = 2
            # hashmap = {1: 1, 3: 4, 2: 3}, array = [[1, 1], [4, 3], [3, 2]]
            # Sort the array of pairs: sortedArr = [[1, 1], [3, 2], [4, 3]]
            
            # 1. [4, 3] is popped   
            # 2. res = [3]      #count = 1
            # 3. [3, 2] is popped   
            # 4. res = [3, 2]   # count = 2

            # nums = [6, 6, 6], k = 1
            # hashmap = {6: 3}, array = [[3, 6]], sortedArr = [[3, 6]]
            # res = [6], count = 1
        
        #E: Time: O(nlogn), Space: O(n)
