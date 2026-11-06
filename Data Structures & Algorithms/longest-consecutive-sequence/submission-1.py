class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #U: Given the nums array, return length of the longest 
        #consecutive sequence of elements that can be formed 

        #M: hashset, arrays, for-while loop, max, conditionals 

        #P: 
            #1. Convert nums array to a hashset
            #2. longest = 0
            #3. for each num in nums: 
                #4. Determine if there is a previous number(num - 1) in hashset
                    #5. If not, that means there is a start of a new sequence
                    #6. currLength = 0
                    #7. while num + currLength in hashset, increase length
                    #8. Outside of while loop, use max function with the longest and length variables
                        #This helps determine the longest sequence in place. 
                        #9. Set result to longest 

            #return longest 
        
        #I: 
        numsSet = set(nums) 
        longest = 0

        for num in numsSet: 
            if (num - 1) not in numsSet: 
                length = 1

                while (num + length) in numsSet: 
                    length += 1
                
                longest = max(length, longest)

        return longest 

        #R: ex: nums = [2, 20, 3, 4, 5]

        #E: Time: O(n), Space: O(n)


