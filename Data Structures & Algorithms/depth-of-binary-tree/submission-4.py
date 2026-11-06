# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #U: Given root of binary tree, return the depth of the tree 
            # depth = # nodes along the longest path from the root to the leaf 
            # of the tree 
        
        #M/P: 
        # Recursive approach 
        # On each recursive call, compare the depths of the left and right subtrees 
        # with the max function 

        #I: 
        if not root: 
            return 0 
        
        depth = 1
        depth += max(self.maxDepth(root.left), self.maxDepth(root.right))
        return depth 

        #R: Example 1

        #E: Time: O(n), Space: O(n)
