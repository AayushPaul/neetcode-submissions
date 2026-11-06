class Solution:
    # Time: 12:10 - 12:38 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #U: Given array nums and integer k, return k most frequent elements within the array. 

        #M/P: 
            # Determine the frequency of each num with hashmap 

            # Sort the hashmap from most frequent to least frequent: 
            # dict(sorted(hashmap.items(), key = lambda item: item[1], reverse = True))

            # Iterate through the sorted hashmap and increase count until it is equal to k. 
                # Use break when count == k
                # While iterating through the hashmap, add the correct keys to a final array. 

            # Return array  

        #I: 
        num_freq = {} 
        for num in nums: 
            num_freq[num] = 1 + num_freq.get(num, 0)
        
        sorted_num_freq = dict(sorted(num_freq.items(), key = lambda item: item[1], reverse = True))

        count = 0 
        final_arr = [] 

        for key in sorted_num_freq: 
            if count == k: 
                break 

            final_arr.append(key) 
            count += 1

        return final_arr 

        #R: nums = [1, 2, 2, 3, 3, 3], k = 2
            # hashmap = {1:1, 2:2, 3:3}
            # sortedHashmap = {3:3, 2:2, 1:1}
                # array = [3, 2]
                # count = 2 = k 
                # break 
            
            # final array = [3, 2]

        #E: Time: O(nlog(n)), Space: O(n)