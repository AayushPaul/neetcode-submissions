class Solution:
    # Time: 12:51 - 1:33
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       #U: Return true if the tree is height-balanced and false otherwise. 

       #M/P: DFS
            # On each recursive call, the height of the left and right subtrees are compared        (abs(isBalanced(root.left) - isBalanced(root.right) <= 1))

       #I:
        def dfs(root): 
            if not root: 
                return [True, 0]

            left = dfs(root.left) 
            right = dfs(root.right) 
            isBalanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [isBalanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

       #R: 

       #E: Time: O(n), Space: O(n) 