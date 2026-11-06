# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Time: 8:36 to 9:48
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #U: Given two nodes from trees p and q, return the lowest common ancestor 
        # of the two nodes (p and q are descendants)

        #M/P: 
            # Base Case: if the root, p, or q node does not exist, return None 

            # Compare root's value with the p and q values 
            # Use recursion to traverse through the left or right nodes based on 
            # the comparision between the root, p, and q values 

            # 1st Case: p's val < root's val < q's val 
                #LCA = root.val 
            
            # 2nd Case: When p.val and q.val < root.val 
                # Recrusively traverse through the left subtree 
            
            # 4th Case: When p.val == root.val and q.val > root.val or q.val < root.val
                # LCA = root.val 
            
            # 3rd Case: When p.val and q.val > root.val
                # Recrusively traverse through the right subtree 

        #I: 

        #Base Case 
        if not root or not p or not q: 
            return None 
        
        #2nd Case 
        if p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val: 
            #3rd Case 
            return self.lowestCommonAncestor(root.right, p, q) 
        else: 
            # Accounts for the 1st and 4th Cases 
            return root 
        
        #E: Time: O(h), Space: O(h)
