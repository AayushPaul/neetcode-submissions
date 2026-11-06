# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Time: 5:43 - 
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #U: Given root, return level order traversal as a nested list 
            # Each sublist contains the values of nodes at particular level in the tree 
        
        #M: BFS 

        #P: 
            # Initialize a final results list 
            # Initialize a queue with a deque 
            # Add the root node to the queue 
            # While queue is not empty, 
                # size of the level or len(queue)
                # Create a for loop that executes some important ops a certain # times(based 
                # on the number of nodes in current level)
                    # Pop node from front of the queue (represents a parent node)
                    # append child nodes to queue and their node values to sublist based on left and right child availability
                        # This requires some conditionals(ex: if left child only exists, we add
                        # the left child to the queue only)
                
                # After for loop, add sublist to the results list 
            
            # Return results list 
        
        #I: 
        if not root: 
            return [] 

        results = []
        queue = deque() 
        queue.append(root)

        while queue: 
            level_size = len(queue)
            sublist = []
            
            for _ in range(level_size): 
                node = queue.popleft() 
                sublist.append(node.val)

                if node.left and not node.right: 
                    queue.append(node.left)
                
                if node.right and not node.left: 
                    queue.append(node.right)
                
                if node.left and node.right: 
                    queue.append(node.left)
                    queue.append(node.right)
            
            results.append(sublist)
        
        return results 

            