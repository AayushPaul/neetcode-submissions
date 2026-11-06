class Solution:
    # Time: 7:35 - 
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #U: Return true if it is height-balanced and false otherwise. 
            # height-balanced: left and right subtrees of every node differ in height by no more than 1
        
        #M/P: Find height of left and right subtrees (DFS) 
        # Keep track of height and whether the tree is balanced simultaneously with an array. 

        #I: 
        def dfs(root): 
            if not root: 
                return [True, 0] 

            left = dfs(root.left) 
            right = dfs(root.right) 
            height = 1 + max(left[1], right[1])

            if left[0] and right[0] and abs(left[1] - right[1]) <= 1: 
                return [True, height]
            else: 
                return [False, height]

        return dfs(root)[0]
