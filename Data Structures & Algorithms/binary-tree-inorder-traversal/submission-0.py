# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #12:11 - 
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #U: Return the inorder traversal of nodes' values 

        #M/P: 
            # 1. Traverse the left subtree (left to right) 
            # 2. Parent node 
            # 3. Traverse the right subtree 

            # Recursion 

        #I: 
        array = [] 

        def inorder(node): 
            if not node: 
                return None

            inorder(node.left) 
            array.append(node.val) 
            inorder(node.right)

        inorder(root) 
        return array 

        #R: root = [1,2,3,4,5,6,7]

            # output = 
                # array = [4, 2, 5, 1, 6, 3, 7]

        #E: Time: O(n), Space: O(n) 