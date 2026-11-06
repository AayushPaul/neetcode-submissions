class Solution:
    # Time: 2:30 - 
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #U: Given root node of BST and key, delete node with given key in BST, if present. 
            # Return root node of updated BST 

        #M/P: 
            # Base Case: if not root, return None 

            # If key value > current root/node's value, program has to traverse the right subtree 
            # If key value < current root/node's value, program has to traverse the left subtree 


        #I: 
        if not root: 
            return None 
        
        if key > root.val: 
            root.right = self.deleteNode(root.right, key)
        elif key < root.val: 
            root.left = self.deleteNode(root.left, key)
        else: 
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            nextNode = root.right 
            while nextNode.left:
                nextNode = nextNode.left
            root.val = nextNode.val # Ex 1(3 -> 4)
            root.right = self.deleteNode(root.right, nextNode.val)

        return root

        #R: Example 1 (key: 3)

            #       6     
            #      / \
            #     4   9
            #    / \
            #   1   5

        #E: Time: O(h), Space: O(h) 