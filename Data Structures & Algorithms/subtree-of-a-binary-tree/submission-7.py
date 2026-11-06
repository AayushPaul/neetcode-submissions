class Solution:   
    # Time: 10:35 - 11:43 (Barely saw the code at the beginning) 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #U: Return true if there is subtree of root with same structure and node values as subroot 

        #M/P: 
        # Edge Cases: 
            # If root is NOT null, but subroot is null: return True 
            # If root is null, but subroot is NOT null: return False 
            # Both are null: return True 
        # Otherwise, recruse through left subtree and right subtree of root.
        # DFS Separate function (determines if subtree is equivalent to subroot - boolean function) 

        #I: 
        if not subRoot: 
            return True 
        
        if not root: 
            return False 
        
        if not root and not subRoot: 
            return True 
        
        if self.isSameTree(root, subRoot): 
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    #Compares the subTree and subRoot 
    def isSameTree(self, subTree: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        # M/P: Three edge cases that make the subTree of Tree and subRoot NOT the same! 
            # After checking for base case(which returns True) and edge cases that return False, detemine left subTree and right subTree. 

        #I: 
        # Base Case 
        if not subTree and not subRoot: 
            return True 
        
        if not subRoot or not subTree: 
            return False 

        if subTree.val != subRoot.val: 
            return False 
        
        leftSubTree = self.isSameTree(subTree.left, subRoot.left)
        rightSubTree = self.isSameTree(subTree.right, subRoot.right) 
        
        return leftSubTree and rightSubTree
    
    #E: Time: O(n + m), Space: O(n + m)