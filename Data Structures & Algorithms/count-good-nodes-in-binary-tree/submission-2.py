# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: 10:50 - 
    def goodNodes(self, root: TreeNode) -> int:
        #U: A node x is considered good if path from the root of the tree to the node x contains 
        # no nodes with value greater than value of node x

        # Return # good nodes within the tree 

        #M/P: DFS
            # Intitialize count variable 

        #I: 

        count = 0

        def dfs(node, maxVal):
            if not node: 
                return 0  

            nonlocal count 
            
            if node.val >= maxVal: 
                count += 1
            
            newMax = max(maxVal, node.val)

            dfs(node.left, newMax)
            dfs(node.right, newMax)

            return count 

        return dfs(root, root.val)

        #R: Example 1

        #E: Time: O(n), Space: O(n)
        