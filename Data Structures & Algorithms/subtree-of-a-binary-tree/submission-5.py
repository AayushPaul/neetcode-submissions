class Solution:   
    # Time: 6:08 - 6:51 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #U: Return true if there is subtree of root with same structure and node values as subroot 

        #M/P: 
        # 1. Edge Cases 
        # If root is NOT null, but subroot is null: return True 
        # If root is null, but subroot is NOT null: return False 
        # Both are null: return True 

        # DFS Separate function (determines if subtree is equivalent to subroot - boolean function) 

        #I: 
        if not root and not subRoot: 
            return True 

        if not subRoot: 
            return True 
        
        if not root: 
            return False 
        
        if root.val == subRoot.val: 
            if self.isSameTree(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, subTree: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        #Base Case
        if not subTree and not subRoot: 
            return True 

        #Edge Cases
        if not subTree or not subRoot or subTree.val != subRoot.val: 
            return False 
        
        leftSubTree = self.isSameTree(subTree.left, subRoot.left)
        rightSubTree = self.isSameTree(subTree.right, subRoot.right)

        return leftSubTree and rightSubTree
    
    # Time: O(n * m), Space: O(n * m) 