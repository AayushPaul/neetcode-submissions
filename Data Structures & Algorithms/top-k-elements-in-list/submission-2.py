class Solution:
    # Time: 4:00 - 5:05
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # U: Given nums array and integer k, return k most 
        # freq elements within array 

        #M/P: 
            # Use hashmap to keep track of the frequency of numbers 
            # Create an array where the count or freq of each number is the index 
            # and the values at those indices are the numbers(keys) 

            # Iterate through the frequency array backwards and keep adding the 
            # numbers in the frequency array to the final result array; 
            # if len(res) == k at any points, return res array 

            # return answer array 

        #I: 
        count = {}
        freqArr = [[] for i in range(len(nums) + 1)]
        res  = []

        for num in nums: 
            count[num] = 1 + count.get(num, 0)
        
        # Creates the freq array 
        for num, cnt in count.items(): 
            freqArr[cnt].append(num) 
        
        for i in range(len(freqArr) - 1, 0, -1):
            # Edge Case (When there is more than one number with the 
            # same frequency) 
            for num in freqArr[i]: 
                res.append(num)

                if len(res) == k: 
                    return res
        
        #R: 
        
        #E: 
        #Time: O(n), Space: O(n)