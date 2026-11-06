class Solution:
    #Time: 12:10 - 12:26 (finished writing the code at 12:20)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #U: Given roots of p and q, return true if trees are equivalent; else, return false 

        #M/P: 

        #I: 
        if not p and not q: 
            return True 
        
        if not p or not q or p.val != q.val:  
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        #E: Time: O(n), Space: O(n)