class Solution:
    #Time: 8:13 PM - 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #U: Diameter: length (# edges) of the longest path between any two nodes within tree 
        # pass does not necessarily have to pass through the root 

        # Return diameter 

    #M/P: DFS
        # Keep track of longest length (diameter) with max function
        # left = traverse through left subtree of each node 
        # right = traverse through right subtree of each node 

        # Inside dfs function, keep track of the current number of edges 

    #I:
        diameter = 0 

        def dfs(root): 
            nonlocal diameter
            if not root: 
                return 0  
            
            left = dfs(root.left) 
            right = dfs(root.right) 

            diameter = max(diameter, left + right)
            return 1 + max(left, right) 
        
        dfs(root)
        return diameter