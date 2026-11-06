# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #U: Return true if the height of the tree is balanced and false otherwise
            # height-balanced tree: the difference in the height for each node's 
            # left and right subtrees is not more than 1 (<= 1)
        
        #M/P: 
            # Recursive; update height when traversing through each node/subtree 

        #I: 
        leftHeight, rightHeight = 0, 0 

        #Base Case 
        if not root: 
            return True 
        
        # I probably need to create another function that determines the height 
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        # Diff between the height of the left and right subtrees is > 1
        if abs(leftHeight - rightHeight) > 1: 
            return False 

        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self, curr: Optional[TreeNode]) -> int: 
        if not curr: 
            return 0 
        
        return 1 + max(self.height(curr.left), self.height(curr.right))