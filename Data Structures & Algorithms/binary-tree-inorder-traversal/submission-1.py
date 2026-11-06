# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #10:13 - 10:25 
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #U: Given root, return the inorder traversal of its nodes' values in array format

        #M/P: Inorder DFS function (traverse left subtree, parent, then right subtree)

        #I: 
        array = [] 

        def inorder(currNode): 
            if not currNode: 
                return [] 

            inorder(currNode.left) 
            array.append(currNode.val)
            inorder(currNode.right) 

            return array 

        return inorder(root) 

        #R: Example 2

        #E: Time: O(n), Space: O(n) 