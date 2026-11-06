class Solution:
    #Time: 1:51 - 2:30 
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #U: Given root of tree and integer k, return the kth smallest value (1-indexed) in the tree. 

        #M/P: DFS (the nodes are already sorted from left to right because it's a BST)
            # Go through all the nodes in the left and right subtrees with recursion 
            # Keep a count variable: when count == k, return that node's value 

            # Inorder Traversal 

        #I: 
        count = 0
        result = None

        def dfs(curr):
            nonlocal count, result
            if not curr or result is not None:
                return

            dfs(curr.left)
            
            count += 1
            if count == k:
                result = curr.val
                return
            
            dfs(curr.right)
        
        dfs(root)
        return result

    # Time: O(n), Space: O(n) 