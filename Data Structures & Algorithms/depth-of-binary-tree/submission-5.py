# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: 7:22 - 7:36 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0 
        
        depth = 1 
        depth += max(self.maxDepth(root.left), self.maxDepth(root.right)) 
        return depth 

#R: Example 1

#E: Time: O(n), Space: O(h) 