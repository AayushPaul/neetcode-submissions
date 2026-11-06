# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Time: 7:14 - 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #U: Return true if the trees share the same exact structure and 
        # nodes have the same values 

        #M/P: 
            # Base Case: If not p and not q, return True 

            # If p.left != q.left or p.right != q.right, return False 

            # If p.left and not q.left, return True 
        
        #I: 
        if not p and not q: 
            return True 
        
        if p and q and p.val == q.val: 
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else: 
            return False

        #E: Time: O(n), Space: O(n)