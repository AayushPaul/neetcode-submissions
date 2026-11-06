# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Time: 2:50 - 3:15 
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #U: Given root of a BST and integer k, return the kth smallest value (1-indexed) in the tree. 

        #M/P: DFS (inorder search) 
        
        #I: 
        count = 0
        result = 0
        
        def dfs(curr): 
            nonlocal count, result
            
            if not curr: 
                return 
            
            dfs(curr.left) 
            count += 1
            
            if count ==  k: 
                result = curr.val 
                return
                
            dfs(curr.right) 

        dfs(root)
        return result
    
        #R: 
            # Example 2 - ans: 5 (kth or 4th node)
            
                #   4
                #  / \
                # 3   5
            #    /
            #   2