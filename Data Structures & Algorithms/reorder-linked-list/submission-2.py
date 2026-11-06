# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time: 11:16 - 
    def reorderList(self, head: Optional[ListNode]) -> None:
        #U: Reorder the nodes of the LL in the following order: [0, n-1, 1, n-2, 2, n-3, ...] without changing 
        # node values 

        #M/P: Slow and Fast ptr approach
            # Determine 2nd half of LL when fast is either at the last node or at null 
            # At that point, start of 2nd half is slow.next 

            # Reverse 2nd half of LL 

            # Merge the 1st and 2nd halves of LL 

        #I: 
        slow, fast = head, head.next 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
    
        # Reverse the 2nd Half of LL 
        secondHalf = slow.next 
        prev = slow.next = None  

        while secondHalf: 
            tmp = secondHalf.next 
            secondHalf.next = prev 
            prev = secondHalf 
            secondHalf = tmp 
        
        # Merge part
        firstHalf, secondHalf = head, prev 
        while secondHalf: 
            tmp1, tmp2 = firstHalf.next, secondHalf.next 
            firstHalf.next = secondHalf
            secondHalf.next = tmp1
            firstHalf, secondHalf = tmp1, tmp2 

        #R: head = [2, 4, 6, 8, 10]
            # slow.next = 8, fast at null 
            # 8 -> 10 transforms to <- 8 <- 10
            # 2 -> 10 -> 4 -> 8 -> 6 (final ans)
             
        #E: Time: O(n), Space: O(1) 
    