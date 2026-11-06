# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time: 11:06 - 
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next
        
        # Reverse the second half starting from slow.next
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Merge first half and reversed second half
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        #R: 2 -> 4 -> 6 -> 8 -> 10
            # Second half: 10 -> 8, First half: 2 -> 4 -> 6
            # first: 2 -> 10 -> 4 -> 8 -> 6