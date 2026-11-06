class Solution:
    #Time: 7:14 - 7:32 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case 
        if not p and not q: 
            return True 

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    #E: Time: O(n), Space: O(h) 