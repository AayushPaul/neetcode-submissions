# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Time: 11:14 - 
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #U: Given root, return level order traversal as a nested list 
            # Each sublist contains the values of nodes at particular level in the tree 
        
        #M: BFS 

        #P: 
            # Initialize a queue using a deque 
            # Initialize a final array 
            # The size of each level is the len(queue)
            # While queue: 
                # There can be a for loop that is based on the len(queue) or the level size 
                    # sublist can be initialized 
                    # Pop elements that are in the queue and add them to the sublist 
                    # In the for loop, there are different conditions 
                    # 1. If there is only a left child, append the left child to the queue 
                    # 2. If there is only right child, append the right child to the queue 
                    # 3. If both left and right children are available, append both to the queue 

                # Add sublist to the final array 
            
            # Return array 
        
        #I: 
        queue = deque() 
        finalArr = [] 

        #Edge Case 
        if not root: 
            return [] 

        queue.append(root)

        while queue: 
            level_size = len(queue)
            sublist = [] 

            for _ in range(level_size): 
                current = queue.popleft() 

                if current.left and not current.right: 
                    queue.append(current.left)
                elif current.right and not current.left: 
                    queue.append(current.right)
                elif current.left and current.right:  
                    queue.append(current.left)
                    queue.append(current.right)

                sublist.append(current.val)

            finalArr.append(sublist)
        
        return finalArr 

        #Time: O(n), Space: O(n)
        