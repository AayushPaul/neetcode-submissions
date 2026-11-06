# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Time: 12:08 - 12:35  
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #U: Given root, return level order traversal as a nested list (each sublist contains
        # the values of nodes at a particular level, from left to right)

        #M/P: BFS 

        #I: 
        queue = deque() 
        result, first_sub_list = [], [] 
        
        if root: 
            queue.append(root) 
            first_sub_list.append(root.val) 
            result.append(first_sub_list)
        
        while len(queue) > 0: 
            subList = [] 
            for i in range(len(queue)): 
                curr = queue.popleft() 
                
                if curr.left: 
                    leftChild = curr.left 
                    subList.append(leftChild.val)
                    queue.append(leftChild) 
                
                if curr.right: 
                    rightChild = curr.right 
                    subList.append(rightChild.val) 
                    queue.append(rightChild)

            if subList: 
                result.append(subList) 
        
        return result
    
        #R: Example 1
            # queue = () 
            # first_sub_list = [1]
            # subList = []
            # result = [[1], [2,3], [4, 5, 6, 7]]
        
        #E: Time: O(n), Space: O(n) 