# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #U: Return length of the diameter of the tree 
            #diameter: length of the longest path between any two nodes(# edges between them)
            #; may or may not pass through the root 
        
        #M: Recursion, BST 

        #P: 
            #1. Declare a global var for the result 
            #2. #Edge case: when there is no root
                    #return 0
            #3. Create a nested function(depth-first search)
            #4. Go through the left and right subtrees 
            #5. Return max of the current result and left and right values
        
        #I: 
        self.res = 0

        def dfs(curr):
            if not curr: 
                return 0 

            left = dfs(curr.left) 
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.res

        #R: Went through a detailed case

        #E: T(N): O(n), Space: O(h)
