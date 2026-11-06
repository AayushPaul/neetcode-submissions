class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Hashset 
        setNums = set()

        for i in range(len(nums)): 
            if nums[i] in setNums: 
                return True 
            
            setNums.add(nums[i])
        
        return False 