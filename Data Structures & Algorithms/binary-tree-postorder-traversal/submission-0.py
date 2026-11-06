# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Time: 10:40 - 10:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #U: Return postorder traversal of nodes' values 

        #M/P: Postorder dfs function (left subtree, right subtree, root)

        #I: 
        array = [] 

        def postorder(currNode): 
            if not currNode: 
                return []
            
            postorder(currNode.left)
            postorder(currNode.right) 
            array.append(currNode.val) 

            return array 
        
        return postorder(root)

        #R: Example 1

        #E: Time: O(n), Space: O(n) 