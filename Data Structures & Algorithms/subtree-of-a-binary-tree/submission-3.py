# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    #Time: 4:58 - 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #U: Return true if there is subtree of root that is identical to the values 
        # and structure of the subRoot 

        #M/P: 
            # Helper function to check if two trees are identical (isSameTree)
            # When root's value is equal to the subRoot's value, 
            # the helper function will be used with the root and the subroot params

            # In helper function, when the root and subroot are null when the 
            # helper function is called on BOTH the left and right child nodes, that means 
            # the subtree has been found (true gets returned up the recursive call stack) 
        
        #I: 
        def isSameTree(r, sub):  
            if not r and not sub: 
                return True 
            
            # Case: root and subRoot trees both exist and the value of the curr nodes are the same
            if r and sub and r.val == sub.val: 
                return isSameTree(r.left, sub.left) and isSameTree(r.right, sub.right)
            else: 
                return False 
        
        # Edge Case: When subroot is none 
        if not subRoot: 
            return True 

        # When there is no root node, there is no subtree 
        if not root: 
            return False 

        # If not, check recursively in the left OR right subtrees
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        #E: Time: O(n), Space: O(n)