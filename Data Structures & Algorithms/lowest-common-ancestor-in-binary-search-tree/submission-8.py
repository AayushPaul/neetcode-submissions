# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Time: 12:16 - 12:30  
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
       #U: Return lowest common ancestor (LCA) of the two nodes. 

       #M/P: 
            # If p and q values are < root val
                # Program goes to the left subtree of root 
            
            # If p and q values are > root val
                # Program goes to the right subtree of root 

            # Else: 
                # return root

       #I: 
        if p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q) 
        elif p.val > root.val and q.val > root.val: 
            return self.lowestCommonAncestor(root.right, p, q)
        else: 
            return root 

       #R: Example 2
            # Since p and q values are < 5 (first root)
                # Program goes to the left subtree of root (root.left) 

            # The new root val is 3 (root.val == p.val) 
                # return root.val or 3
        
        #E: Time: O(n), Space: O(n) 