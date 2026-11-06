class Solution:
    # Time: 8:15 - 8:46 (without talking out loud and after seeing the solution) 
    def longestConsecutive(self, nums: List[int]) -> int:
        #U: Given nums array, return the length of the longest consec sequence formed

        #M/P: 
            # Convert nums array to a hashset 
            # Create a var (longest) to keep track of the largest length 
            # Go through the nums array with a for loop 
                # If num - 1 not in hashset(there is no left neighbor), it is the start of a new consec
                # sequence. 
                    # Initialize length to 0.
                    # while num + length in hashset, increase length 
                
                # Use max function to compare current val of longest with current val of length and set
                # that to "longest" 
            
            # Return longest length

        #I: 
        numsSet = set(nums) 
        longest = 0 
        
        for num in nums: 
            length = 0
            if (num - 1) not in numsSet:  
                while (num + length) in numsSet: 
                    length += 1
            
            longest = max(length, longest) 
        
        return longest

        #R: 
            # nums = [2, 20, 4, 10, 3, 4, 5], hashset = (2, 20, 4, 10, 3, 5)
            # sequence = [2, 3, 4, 5], length = 4, longest = 4 (ans) 
            # sequence = [20], length = 1
            # sequence = [10], length = 1
        
            # nums = [1], hashset = (1), length = 1, longest = 0 -> 1 (ans) 

            # nums = [2, 2], hashset = (2), length = 0 -> 1, longest = 0 -> 1 (ans) 

        #E: Time: O(n), Space: O(n) 
