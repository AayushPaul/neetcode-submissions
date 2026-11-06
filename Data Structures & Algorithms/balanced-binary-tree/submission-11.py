class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #U: Given binary tree, return true if height is balanced and false otherwise. 
            # height-balanced: left and right subtrees of every node differ in height by no more than 1. 

        #M/P: DFS

            # Base Case
            # left, right = dfs(root.left), dfs(root.right) 
            # 

        #I: 
        def dfs(root): 
            if not root: 
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right) 
            maxHeight = 1 + max(left[1], right[1])  # My Idea

            if left[0] and right[0] and abs(left[1] - right[1]) <= 1: 
                return [True, maxHeight] #Final Ans: [True, 3]
            else: 
                return [False, maxHeight]

        return dfs(root)[0]

        #R: 
        #       1
        #      / \
        #     2   3
        #        /
        #       4

        #E: Time: O(n), Space: O(h)