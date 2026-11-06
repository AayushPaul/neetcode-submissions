# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: 10:35 - 11:13  
    def goodNodes(self, root: TreeNode) -> int:
    #U: Given root of a binary tree root, return # good nodes within the tree. 
        # A node is considered good if the path from the root to the node x contains no nodes with a value > value of node x. 
    
    #M/P: DFS 
        # maxValue var that keeps track of the max value encountered till now from root to each node (x)
        # number of good nodes in tree (global variable) 
    
    #I: 
        num_good_nodes = 0

        def dfs(curr, maxValue): 
            nonlocal num_good_nodes 
            
            if not curr: 
                return
            
            if curr.val >= maxValue: 
                num_good_nodes += 1
            
            maxValue = max(curr.val, maxValue)
                
            dfs(curr.left, maxValue) 
            dfs(curr.right, maxValue)
        
        dfs(root, root.val)
        return num_good_nodes
    
    #E: Time: O(n), Space: O(n) 