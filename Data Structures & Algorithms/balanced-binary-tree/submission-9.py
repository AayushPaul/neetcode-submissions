class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #U: Determine if tree is balanced (left and right subtrees of every node differ in height by no more than 1)
        
        #M/P: Keep track of balance for each node while keeping track of height 

        def dfs(root): 
            if not root: 
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right) 
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]

        #E: Time: O(n), Space: O(h) 
            # Space - balanced: O(logn), skewed: O(n) 