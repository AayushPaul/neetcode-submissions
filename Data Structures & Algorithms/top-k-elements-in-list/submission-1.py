class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] #Keeps track of the frequencies of each number

        for n in nums: 
            #Goes through each number and increases the count of each number
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items(): 
            #Bucket sort 
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1): 
            for num in freq[i]: 
                res.append(num)
                if len(res) == k: 
                    return res

        