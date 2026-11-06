class Solution:
    #Time: 11:07 - 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #U: Diameter of a binary tree = defined as length of the longest path between any 2 
        # nodes within the tree 
            # Length of a path between two nodes in binary tree is number of edges
            # between the nodes; the path cannot include the same node twice. 

        # Return diameter of tree

        #M/P: DFS  

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

        #R: 
    
    #E: 