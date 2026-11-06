class Solution:
    # Time: 12:50 - 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #U: Given nums array and k, return k most frequent elements within 
        # the array. 

        #M/P:
            # Determine the frequency of each number in nums array with hashmap 
            # Sort the hashmap by its values(counts) of each key(elems) 
                # most frequent to least frequent 

            # Get k elements and add them to the final array/return that 
        
        #I: 
        freqMap = {} 

        for num in nums: 
            freqMap[num] = 1 + freqMap.get(num, 0)

        freqArr = [] 
        for elem, count in freqMap.items(): 
            freqArr.append([count, elem])
        freqArr.sort() 

        res = []
        while k > 0: 
            res.append(freqArr.pop()[1])
            k -= 1
        
        return res

        #R: 
            #Ex 1: [1, 3, 3, 4, 4, 4], k = 2
                # freqMap = {1:1, 3:2, 4:3}
                # array = [[1, 1], [3, 2], [4, 3]]
                # array.pop()[0]
                # res = [4, 3]

            #Ex 2: [1, 1, 1, 5, 5, 4, 4, 4, 4], k = 2
                # freqMap = {1:3, 5:2, 4:4}
                # array = [[3, 1], [2, 5], [4, 4]]
                # Sort by count (array.sort()) -> [[2, 5], [3, 1], [4, 4]]
                # array.pop()[1]
                # res = [4, 1]

        #E: Time: O(n), Space: O(n) 