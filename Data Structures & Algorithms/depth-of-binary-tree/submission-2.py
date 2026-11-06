# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #U: Given root of binary tree, we have to return its depth
        #depth: number of nodes along the longest path(similar to height)

        #M: Recursion, max function  

        #P: 
            #1. Initiailize maxDepth to 0 
            #2. If root does not exist, return 0 
            #3. 1 + max(maxDepth(root.left), maxDepth(root.right))

        #I: 
        if not root: 
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        #R: Example 1
