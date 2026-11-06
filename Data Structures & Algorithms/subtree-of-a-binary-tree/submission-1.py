# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper function to check if two trees are identical
        def isSameTree(s, t):
            if not s and not t:
                return True
            if not s or not t or s.val != t.val:
                return False
            return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        # If subRoot is None, it's always a subtree
        if not subRoot:
            return True
        # If root is None, subRoot can't be a subtree
        if not root:
            return False
        # Check if the current trees match, or search in left/right subtrees
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
