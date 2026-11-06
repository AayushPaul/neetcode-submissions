# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #U: Given head of linked list, we have to reorder the nodes of the
        # list such that 

            # Ex: [0, 1, 2, 3, 4, 5, 6]
            # Output: [0, 6, 1, 5, 2, 4, 3]

        #M/P: LL
            # Iterate all the nodes with a while loop and then append each node
            # to a separate list (Purpose: Two Pointer Strategy with L and R)
        
            # After swapping the left node with the right node, we increment left
            # After swapping the right node with the left node, we decrement right
            # This keeps happening until l >= r. 
        
        #I: 
        nodes = [] #Store all the nodes 
        curr = head 

        while curr: 
            nodes.append(curr)
            curr = curr.next 
        
        left, right = 0, len(nodes) - 1

        while left < right: 
            # head = 2 -> 4 -> 6 -> 8 -> 10
            # 1. left at 2, right is at 10 
            # 2. 2 -> 10 
            # 3. Left is at 4, right is at 10 
            # 4. 2 -> 10 -> 4
            # 5. Left is at 4, right is at 8 
            # 6. 2 -> 10 -> 4 -> 8
            # 7. Left is at 6
            # 8. 2 -> 10 -> 4 -> 8 -> 6
            # 9. Right is also at 6. 

            nodes[left].next = nodes[right]
            left += 1

            nodes[right].next = nodes[left] 
            right -= 1
        
        nodes[left].next = None

        #E: 
        # Time: O(n), Space: O(n) 
             

    