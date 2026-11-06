# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #U: Build binary tree from preorder and inorder traversals and return its root. 

        #M/P: Get root first (first node in preorder array: TreeNode(preorder[0]))
            # Build tree from left and right subtrees with recursion (root.left and root.right)
            # mid node = middle node of inorder array 
            
        #I:
        if not preorder or not inorder: 
            return None 

        root = TreeNode(preorder[0])
        midIndex = inorder.index(preorder[0])   #preorder[0] = root 

        root.left = self.buildTree(preorder[1 : midIndex + 1], inorder[:midIndex])
        root.right = self.buildTree(preorder[midIndex + 1:], inorder[midIndex+1:])
        return root 

        #R: Example 1

        #E: Time: O(n^2), Space: O(n) 