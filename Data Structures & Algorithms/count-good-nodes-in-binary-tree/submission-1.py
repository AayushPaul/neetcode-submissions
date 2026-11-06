# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #U: A node x is good if the path from the root of the tree 
        # to the node x contains no nodes with value > value of node x. 

        # Return # of good nodes within the tree. 

        #M/P: 
            # Use DFS to traverse through this tree. 
            # If there is no root node, the tree does not exist, so return 0. 

            # Initialize a count variable and set it to 1 (root)

        #I: 

        def dfs(node, maxVal): 
            if not node: 
                return 0 
            
            if node.val >= maxVal: 
                count = 1
                maxVal = max(maxVal, node.val) 
            else: 
                count = 0 

            count += dfs(node.left, maxVal)
            count += dfs(node.right, maxVal)

            return count 

        return dfs(root, root.val)