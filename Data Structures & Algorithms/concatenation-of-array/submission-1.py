class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #U: Create array ans of length 2n where n is size of nums array 
            #ans is concatenation of 2 nums arrays 

        #M/P: 

        #I: 
        return nums + nums

        # Another Solution: 
        # ans = []
        # for i in range(2): 
            # for num in nums:  #This happens twice 
                # ans.append(num) 
        
        # return ans

        #E: 
            #Time: O(n), Space: O(n)