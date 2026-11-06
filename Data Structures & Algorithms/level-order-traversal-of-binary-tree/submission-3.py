# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Time: 4:00 - 
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #U: Given root of tree, return level order traversal of the tree as a nested list 
        # (each sublist contains the values of nodes at particular level in the tree)
        # Traverse from left to right. 

        #M/P: BFS (queue/deque)
            # Initialize a list/array 
            # Initialize a queue/deque 
            # If root is null, return [] (edge case) 

            # If root, append the root node's value to the queue
            # While len(queue) > 0
                # for loop that iterates through the current queue/nodes at that level 
                    # Pop leftmost element from queue and add to sublist
                    # If left child exists, add left child's value to the queue 
                    # If right child exists, add right child's value to the queue 
            
            # Return final array 

        #I: 
        finalList = [] 
        queue = deque() 

        if not root: 
            return [] 
        
        queue.append(root) 

        while len(queue) > 0: 
            subList = [] 
            for i in range(len(queue)): 
                currElem = queue.popleft() 
                subList.append(currElem.val) 

                if currElem.left: 
                    queue.append(currElem.left)

                if currElem.right: 
                    queue.append(currElem.right)
            
            finalList.append(subList) 
        
        return finalList 
                
        #R: Example 1
        #            1        # array = [[1], [2, 3], [4, 5, 6, 7]] 
        #          /  \       # queue = (4, 5, 6, 7)
        #         2    3      # previous level queue = (2, 3) 
        #        / \  / \
        #       4   5 6  7

        #E: Time: O(n), Space: O(n)