# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    # Time: 9:05 - 9:43 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #U: Given the roots of 2 binary trees root and subRoot, return true if there is a subtree 
        # of root with same structure and node values of subRoot and false otherwise. 

        #M/P: 

        #I: 
        
        #Edge Cases 
        if not subRoot: 
            return True 

        # Root does not exist, but subroot exists. 
        if not root: 
            return False 
        
        if self.sameTree(root, subRoot): 
            return True 
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 

    #DFS/helper function 
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        if not root and not subRoot: 
            return True 
        
        if root and subRoot and root.val == subRoot.val: 
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)

        return False 

    #E: Time: O(n), Space: O(n)