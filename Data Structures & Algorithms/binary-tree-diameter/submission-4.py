class Solution:
    #Time: 11:51 PM - 12:21 PM 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #U: Diameter: Length of the longest path between any two nodes within tree 

        # Length of a path: number of edges between the nodes 
        # Return diameter of tree 
    
    #M/P: 
        # Use DFS 
        # Keep track of the max length with max function 

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