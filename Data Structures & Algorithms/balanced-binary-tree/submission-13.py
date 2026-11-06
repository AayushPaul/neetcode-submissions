class Solution:
    # Time: 11:15 - 12:03
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #U: Return true if tree is height-balanced and false otherwise. 
            # height-balanced binary tree: left and right subtrees of every node differ 
            # in height by no more than 1

        #M/P: 


        #I: 
        def dfs(root): 
            if not root: 
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right) 
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

        #R: 
            #   1
            #  / \      #height of left = 1, height of right = 3 (abs(1-3) = 2 > 1)
            # 2   3
            #    /
            #   4
            #  /
            # 5