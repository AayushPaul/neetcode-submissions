# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#
class Solution:
    # Time: 12:20 - 12:33
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #U: Given root of binary tree, return its depth. 

        #M/P: 
            # Edge case: if zero nodes present, return 0 
            # Iterate through the left and right subtrees 
                # Depth = depth of either left or right subtree (based on which one is higher)
                # Use the max function 
        
        #I: 
        if not root: 
            return 0 
        
        depth = 1
        depth += max(self.maxDepth(root.left), self.maxDepth(root.right)) 
        return depth 

        #R: Example 1

        #E: Time: O(n), Space: O(n)