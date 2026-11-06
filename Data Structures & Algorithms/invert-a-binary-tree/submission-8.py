# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: 12:05 - 12:12 
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #U: Invert binary tree and return its root. 

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

        #R: 

        #E: Time: O(n), Space: O(n)