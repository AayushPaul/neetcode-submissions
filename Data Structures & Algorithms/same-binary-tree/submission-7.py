class Solution:
    #Time: 7:50 - 8:04 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #U: Return true if the trees are equivalent. Otherwise, return False 

        #M/P: 
            # 1. Check if the corresponding values are equal. 
            # 2. Check if the structure is equal. 

        #I: 
        if not p and not q: 
            return True 

        if p and q and p.val == q.val: 
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False 

        #E: Time: O(n), Space: O(h) 