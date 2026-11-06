# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: 4:58 - 
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #U: After inserting new node with val, return root node of BST after insertion. 

        #M/P: 

        # Base Case: If root DNE, add new node to tree with the TreeNode class 
            # If val > root.val, traverse right subtree
            # If val < root.val, traverse left subtree 

        #I: 
        if not root: 
            return TreeNode(val)

        if val > root.val: 
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val: 
            root.left = self.insertIntoBST(root.left, val)
        
        return root 

        #R: Example 1 (with the values of 2 and 6)

        #E: Time: O(n), Space: O(n) 