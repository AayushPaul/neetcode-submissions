class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #U: Given root of a binary tree, return only values of nodes that are visible from right side of the tree in a list.
        
        #M/P: BFS (deque) 
            # Use the normal approach 
                # Consider edge case where there are no nodes (return []) 
                # On each level, add the right most node to the final array 
                
        #I: 
        if not root: 
            return [] 
        
        queue = deque() 
        queue.append(root) # 1 
        result = [] 
        
        while len(queue) > 0: 
            level_len = len(queue)
            for i in range(level_len): 
                curr = queue.popleft() 
                
                if i == level_len - 1: # Right most node on level 
                    result.append(curr.val)

                if curr.left: 
                    queue.append(curr.left) 
                
                if curr.right: 
                    queue.append(curr.right) 
                
        return result 
    
        #R: Example 1
            # curr = 5, queue = () 
            # result = [1, 3, 5]
        
        #E: Time: O(n), Space: O(n) 