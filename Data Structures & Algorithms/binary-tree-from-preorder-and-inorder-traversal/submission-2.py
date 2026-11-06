# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #U: Rebuild the binary tree from the preorder and inorder traversals 

        #M/P: 
            #Preorder: Current, Left, Right 
            #Inorder: Left, Current, Right

        # Root is preorder[0]. Use the TreeNode class on preorder[0] 
        # Get mid index (root's index from inorder array)
        
        # Left subtree(root.left) occurs when preorder array from root index to index of the right child
        # (mid + 1) (exclusive) and when inorder array starts from first index until the mid index (excluded)

        # Right subtree(root.right) 

        #I: 

        if not preorder or not inorder: 
            return None 

        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)   #Gets index of the root val as that is the dividing point between 
                                        # the left and right subtrees 

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root 

        #E: Time: O(n^2), Space: O(n)
