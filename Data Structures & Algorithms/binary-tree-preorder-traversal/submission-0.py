# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Time: 10:30 - 10:36
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #U: Return preorder traversal of nodes' values 

        #M/P: Root, Left subtree, Right subtree (preorder dfs function)

        #I: 
        array = [] 

        def preorder(currNode): 
            if not currNode: 
                return [] 
            
            array.append(currNode.val) 
            preorder(currNode.left)
            preorder(currNode.right) 

            return array
        
        return preorder(root)