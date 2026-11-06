# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Time: 4:13 - 4:51 
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #U: Given root of a BST and an integer k, return kth smallest value (1-indexed) in the tree. 

        #M/P: Inorder Search (left subtree, root node, right subtree) 
            # count = 0 
            # result = 0 (result = value of kth smallest node, so result is returned)
            # Create inner dfs function 
                # dfs(curr.left) # curr = current node 
                
                # count += 1

                # Check if count == k: 
                    # result = curr.val 
                    # return result 

                # dfs(curr.right)

            #  return dfs(root) 

        #I: 
        count, result = 0, 0 

        def dfs(curr): 
            nonlocal count
            nonlocal result 

            if not curr: 
                return 

            dfs(curr.left) 
            count += 1

            if count == k: 
                result = curr.val 
                return
            
            dfs(curr.right) 

        dfs(root) 
        return result 

        #R: Example 2

        #E: Time: O(n), Space: O(n)