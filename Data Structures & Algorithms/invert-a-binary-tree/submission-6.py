# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: 6:40 - 6:57 
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #U: Given root of binary trew, invert the binary tree and return its root 
        
        #M/P: Switch the left and right nodes with recursion 
        if not root: 
            return None 
        
        tmp = root.left 
        root.left = root.right 
        root.right = tmp 
        
        self.invertTree(root.left) 
        self.invertTree(root.right)
        
        return root 