# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time: 12:25 - 1:23
    def reorderList(self, head: Optional[ListNode]) -> None:
        #U: Reorder the nodes in this order: [0, n-1, 1, n-2, 2, n-3, ...]

        #M/P: Slow and Fast ptrs to iterate through LL in first pass (while fast and fast.next)
        # After while loop, slow.next is 2nd half of LL; reverse 2nd half 

        # Go through first half of LL, adding nodes from the 2nd half in order 

        #I: 
        slow, fast = head, head 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
        
        #Reverse 2nd half of List 
        secondHalf = slow.next 
        prev = slow.next = None 

        while secondHalf: 
            tmp = secondHalf.next 
            secondHalf.next = prev 
            prev = secondHalf
            secondHalf = tmp 

        #Merge first and second halves 
        firstHalf, secondHalf = head, prev 

        while secondHalf: 
            tmp1, tmp2 = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf 
            secondHalf.next = tmp1 
            firstHalf, secondHalf = tmp1, tmp2  


        #R: 2 -> 4 -> 6 -> 8 -> 10
            # Slow at 6, Fast at 10 (fast.next is null)
            # Reverse 2nd half of LL starting from 8 (slow.next) 

            # 2 -> 4 -> 6 -> (crossed off - slow.next) <- 8 <- 10
            # Final: 2 -> 10 -> 4 -> 8 -> 6
        
        #E: Time: O(n), Space: O(1) 