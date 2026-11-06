class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # U: Return max path sum of any non-empty path (NOT BST) 

        #M/P: DFS
            # Use max function to keep track of the current max path sum.   
            # Postorder Traversal (left subtree, right subtree, root) 

        #I: 
        maxSum = float('-inf') 

        def dfs(curr): 
            nonlocal maxSum

            if not curr: 
                return 0 
            
            # Only include branch if it contributes a positive value
            leftMax = max(dfs(curr.left), 0)
            rightMax = max(dfs(curr.right), 0)

            # Path that splits at the current node
            priceNewPath = curr.val + leftMax + rightMax
            maxSum = max(maxSum, priceNewPath)

            # Return the max gain this node can contribute to its parent
            return curr.val + max(leftMax, rightMax)

        dfs(root)
        return maxSum

        #R: Example 1

        #E: Time: O(n), Space: O(n) 