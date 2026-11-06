class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #U: Given root of a binary tree, return true if it is valid binary search tree,       otherwise return false 
        
        #M/P: DFS 
        
        #I: 
        def valid(node, left, right): 
            if not node: 
                return True 

            if not (left < node.val < right): 
                return False 
            
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        
        return valid(root, float('-inf'), float('inf'))
    
        #E: Time: O(n), Space: O(n)