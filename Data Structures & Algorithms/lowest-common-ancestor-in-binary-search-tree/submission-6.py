# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Time: 4:00 - 
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #U: Given BST, return Lowest Common Ancestor of 2 nodes. 
            #LCA between 2 nodes p and q == lowest node in Tree T st both p and q act as descendants
            # Note: BST - nodes are ordered from left to right 

        #M/P: Recursion 
            # If the values of p and q are < root's val (use max function), traverse left subtree (root.left)
            # If the values of p and q are > root's val (use min function), traverse right subtree (root.right)

            # Return root (assuming previous 2 cases do not apply)

        #I: 
        if not root: 
            return None 

        if max(p.val, q.val) < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val: 
            return self.lowestCommonAncestor(root.right, p, q)
        else: 
            return root 

        #R: Example 2

        #E: Time: O(n), Space: O(h) 