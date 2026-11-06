# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Edge case: root does not exist 
        if not root: 
            return 0
        
        rightSubTree = self.maxDepth(root.right)
        leftSubTree = self.maxDepth(root.left)
        #Recursively calls the maxDepth function on right and left subtrees 
        return 1 + max(rightSubTree, leftSubTree)