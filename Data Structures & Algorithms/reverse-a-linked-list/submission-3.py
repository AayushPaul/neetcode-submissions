# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Time: 11:02 - 11:28 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #U: Reverse the LL 

        #M/P: prev, current ptrs 
            # prev is before first node, current is at the first node (head)
            # current ptr points backward (current.next = prev), current is set to current.next 

        #I: 
        curr, prev = head, None 

        while curr: 
            tempNode = curr
            nxt = curr.next 
            curr.next = prev 
            curr = nxt  
            prev = tempNode 

        return prev 

        #R: head = [0, 1, 2, 3] (0 -> 1 -> 2 -> 3), output = [3, 2, 1, 0] (3 -> 2 -> 1 -> 0)

            # <- 0 <- 1 <- 2 <- 3
        
        #E: Time: O(n), Space: O(1)