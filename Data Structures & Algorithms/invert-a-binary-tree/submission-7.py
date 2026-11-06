# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: 12:22 - 12:30 
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #U: Given root of binary tree, invert binary tree and return its root. 

        #M/P: 


        #I: 
        if not root: 
            return None 
         
        tmp = root.left 
        root.left = root.right
        root.right = tmp 

        self.invertTree(root.left) 
        self.invertTree(root.right)

        return root 