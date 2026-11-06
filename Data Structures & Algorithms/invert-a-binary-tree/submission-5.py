# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #U: Given root of the binary tree, invert the binary tree 
        # and return its root 

        #M/P: 
            # if there is no root, return None (base case) 

            # root.left = root.right 
            # root.right = root.left 

            # Recursively call root.left and root.right 

            #Return root 

        #I: 
        if not root: 
            return None 

        tmp = root.left # 2
        root.left = root.right # 2 -> 1
        root.right = tmp # 1 -> 2

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root 

        #E: Time: O(n), Space: O(n)