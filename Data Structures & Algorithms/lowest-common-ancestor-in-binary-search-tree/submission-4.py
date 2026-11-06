# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Time: 9:24 - 
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #U: Given a BST where all node values are unique and two nodes from the tree p and q, 
        #return the lowest common ancestor of both nodes 

        #M/P: 
            #Cases: 
                #1. p is a root(root.val == p.val) and q is p's right child or left child 
                    # return p 
                
                #2. q is a root(root.val == q.val) and p is q's right child or left child 
                    # return p 

                #3. Return root 

        #I: 
        if p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q) 
        elif p.val > root.val and q.val > root.val: 
            return self.lowestCommonAncestor(root.right, p, q) 
        elif root.val == p.val: 
            return p 
        elif root.val == q.val: 
            return q
        else: 
            return root