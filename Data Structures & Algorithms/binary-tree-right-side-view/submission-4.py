class Solution:
    # Note: 11 min break 
    #Time: 12:13 - 
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #U: Return values of nodes visible from right side of tree. 

        #M/P: BFS(deque) 

        #I: 
        if not root:
            return [] 
        
        finalList = [] 
        queue = deque() 
        queue.append(root) 

        while len(queue) > 0: 
            levelSize = len(queue)

            for i in range(levelSize): 
                elem = queue.popleft() 

                if i == levelSize - 1: 
                    finalList.append(elem.val)
                
                if elem.left: 
                    queue.append(elem.left) 
                
                if elem.right: 
                    queue.append(elem.right) #queue = (), finalList = [1, 3, 5]

        return finalList

        #R: Example 1

        #E: Time: O(n), Space: O(n) 