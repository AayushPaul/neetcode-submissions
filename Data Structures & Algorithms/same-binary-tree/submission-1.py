# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #U: Given roots of 2 binary trees p and q, return true if trees are 
        #equivalent, otherwise return false 
        
        #M: Binary Tree, recursion, DFS 

        #P: 
            #1. If p and q do not exist, we have to return True(equivalent trees) 
            #2. If p and q exists and the root nodes are equivalent(p.val == q.val)
                #3. Use recursion on the left and right subtrees 
            #4. Else, return false 
        
        #I: 
        
        #The trees do not exist (base case)
        if not p and not q: 
            return True 

        if p and q and p.val == q.val: 
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else: 
            return False 

        #R: Example 1

        #E: Time: O(n), Space: O(n)
