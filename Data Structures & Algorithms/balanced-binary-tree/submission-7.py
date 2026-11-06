# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #U: Return true if the tree is height balanced and false 

        #M/P: 
            # If there is no root or tree, return True (edge case) 
        
            # Helper function that keeps track of the height between nodes 
            # Call the height helper function in the isBalanced function with root.left and root.right 
            
            # Store the heights between the root and left subtree and the root and the right subtree in 
            # respective variables (leftHeight and rightHeight)
            
            # If at any point in the program the difference between the left and right heights > 1, return False 

            # Eventually, if the program does not return False at any point and the program reaches the point 
            # where there are no more nodes to traverse in the tree, the program reaches the base case, so it 
            # returns True. 
        
        #I: 
        if not root: 
            return True 

        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        #Base Case 
        # if leftHeight == 0 and rightHeight == 0: 
        #     return True 

        if abs(leftHeight - rightHeight) > 1: 
            return False 

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root: Optional[TreeNode]) -> int: 
        if not root: 
            return 0 

        return 1 + max(self.height(root.left), self.height(root.right))
    
    #Time: O(n^2), Space: O(h) where h is the height 