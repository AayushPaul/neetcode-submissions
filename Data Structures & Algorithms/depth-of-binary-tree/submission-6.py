# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: 12:34 - 12:40 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #U: 

        #I: 
        if not root: 
            return 0 

        depth = 1
        depth += max(self.maxDepth(root.left), self.maxDepth(root.right))
        return depth