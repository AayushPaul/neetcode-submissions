class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True 
        
        diff = self.height(root.left) - self.height(root.right) 

        if abs(diff) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True 
        
        return False

    def height(self, root: Optional[TreeNode]) -> int: 
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))