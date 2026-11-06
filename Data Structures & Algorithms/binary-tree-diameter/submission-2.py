class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #U: Diameter of binary tree - defined as length of the longest path between any 2 nodes in the tree 
        # length: # edges between the 2 nodes (path cannot include the same node twice) 
        # Return the diameter of tree 

    #M/P: 
        # Keep track of the count of the edges and take the max count 
        # Return the maxCount (python max function) 
    
        # DFS problem (inner DFS function that goes down each level of the tree)
    
    #I: 
        if not root: 
            return 0 
        
        maxCount = 0
        
        def dfs(root): 
            nonlocal maxCount
            if not root:
                return 0
            
            left = dfs(root.left) 
            right = dfs(root.right) 
            maxCount = max(maxCount, left + right)
            return 1 + max(left, right)
        
        dfs(root) 
        return maxCount