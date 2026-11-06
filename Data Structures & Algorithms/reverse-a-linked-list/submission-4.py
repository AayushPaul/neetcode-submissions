# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Time: 1:37 - 2:03 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #U: Given head, reverse the list, and return the new beginning of the list 

        #M/P: Have two pointers (curr and prev)
            # While curr is NOT null 
                # The curr ptr traverses the LL and switches the direction of each arrow. 
                # The prev ptr starts before the LL
                    # On each iteration, the prev ptr moves to the node where the curr ptr was at before the curr ptr moved 
                    # on to the next node.  

        #I: 
        curr, prev = head, None 

        while curr: 
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp 

        return prev 

        #R: 0 -> 1 -> 2 -> 3
            # <- 0 <- 1 <- 2 <- 3
            # prev is at 3, and curr is at null position now 
            # So, prev or 3 is returned. 
        
        #E: Time: O(n), Space: O(1) 