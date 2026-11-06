class Solution:
    # Time: 4:00 - 5:05
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # U: Given the nums array and integer k, return the k most freq elems 
        # within the array 

        #M/P: 
            # Iterate through the nums array with a for loop and 
            # then store the counts in a frequency map 

            # Iterate through the items and add [count(key), num(value)] to a 
            # new array; sort that array 

            # While k != 0, 
                # Pop the values from that array and add that value to the results
                # array 
                # Decrement k
        
        #I: 
        res = []

        freqMap = {} 
        for num in nums: 
            if num not in freqMap: 
                freqMap[num] = 1
            else: 
                freqMap[num] += 1

        arr = [] 
        for num, count in freqMap.items(): 
            arr.append([count, num])
        
        arr.sort() 

        while k != 0: 
            res.append(arr.pop()[1])
            k -= 1
        
        return res 

        #R: 
        # Example 1: [1, 2, 2, 3, 3, 3], arr = [[1, 1], [2, 2], [3, 3]], 
        # res = [3, 2]

        # Example 2: k = 2, [4, 4, 4, 4, 3, 3, 2], freqMap = {4 : 4, 3: 2, 2: 1}, 
        # arr = [[4, 4], [2, 3], [1, 2]], newArr = [[1, 2], [2, 3], [4, 4]], 
        # res = [4, 3]

        #E: Time: O(nlogn), Space: O(n)