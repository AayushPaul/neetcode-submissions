# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #U: Diameter: length of the longest path between any 2 nodes within the tree
            # length of a path = number of edges between 2 nodes (path cannot include same node twice)
            # Given root, return the diameter of the tree 
        
        #M/P: 
            #Keep track of the length in each recursive call with max function 
            #Create a nested/helper function that does this. 
            
            #If there is left child, program should move to the left child and keep track of the length 
            #If there is right child, program should move to the right child and keep track of the length 

            # Use DFS(that should be the helper function)
                # Determine height of left children by calling the dfs function recursively 
                # Determine height of right children by calling the dfs function recursively 

                # Keep track of the length with the max function; return 1 + max(left, right)


            #Return the helper function at the end 

        #I: 
        self.length = 0 # global variable 

        def dfs(curr): 
            #Edge Case: No node is present in the tree 
            if not curr: 
                return 0 
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            self.length = max(self.length, left + right) #Determines the diameter 
            return 1 + max(left, right) #Determines the current height of the tree from the root; needed for 
            # left and right variables 

        dfs(root)
        return self.length