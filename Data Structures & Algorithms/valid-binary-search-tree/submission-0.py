class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Time: 5:02 - 
        def innerValid(node, min_val=float('-inf'), max_val=float('inf')):
            if not node: # Base Case 
                return True 

            if not (min_val < node.val < max_val):
                return False
        
            left_valid = innerValid(node.left, min_val, node.val) 
            right_valid = innerValid(node.right, node.val, max_val) 

            return left_valid and right_valid 

        return innerValid(root)

        #R: Example 1

        #E: Time: O(n), Space: O(n) 