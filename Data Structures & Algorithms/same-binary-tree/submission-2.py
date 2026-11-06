# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #U: Return true if the trees are equivalent; else return False 
            # They have the same structure and the nodes have the same values. 

        #M/P: 
            # Binary trees and recursion 
            # Edge case: If either root is null, return False 
            # Edge case: If both roots are null at that point in the program, 
            # return True (stopping point of the recursive program)

            # On each recursive call, check left and right nodes of each tree 

        #I:
        
        # Stopping point in recursive call 
        if not p and not q: 
            return True 

        if p and q and p.val == q.val: 
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else: 
            return False # Case: Structures of the trees are not same(either p or q is null) 
                         # or values of the nodes are not same

        #R: Example 3 

        #E: Time: O(n), Space: O(n)
