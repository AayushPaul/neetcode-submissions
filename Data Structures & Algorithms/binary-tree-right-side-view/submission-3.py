# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Time: 11:20 - 
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #U: Given root of the tree, return only values of the nodes that are visible from the right 
        # side of the tree. 

        #M: BFS 

        #P: 
            # Initialize a queue to keep track of the nodes encountered in each level 
            # Initialize the array that will be returned 

            # I should append the root to the node. 
            # While queue: 
                # curr = queue.popleft() 

                # If right child of current node exists, I append the right child to the queue  

                # Append the value of the current node to the final array 
            
            # Return final array 
        
        #I: 
        queue = deque() 
        array = [] 

        #Edge Case: 
        if not root: 
            return [] 
        
        queue.append(root)

        while queue:    
            rightSide = None 

            for i in range(len(queue)): 
                node = queue.popleft() 

                if node: 
                    # Set rightSide variable = node 
                    # Append left and right nodes, including null nodes 
                    rightSide = node 
                    queue.append(node.left)
                    queue.append(node.right)

            #If rightSide is not None, append the value of the node stored in rightSide var to the array 
            if rightSide: 
                array.append(rightSide.val)
            
        # Return final array 
        return array

        #E: Time: O(n), Space: O(n)