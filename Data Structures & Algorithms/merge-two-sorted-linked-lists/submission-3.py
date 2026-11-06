# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time: 12:22 - 
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #U: Merge the 2 lists into one sorted LL and return head of the new sorted linked list 

        #M/P: Initialize dummy node; the head of the merged list is dummy.next, so that is returned 
            # Initialize a pointer called curr that moves through the merged list; initially set to dummy node

            # If only list1 is null, add the rest of list2 to the merged list. 
            # If only list2 is null, add the rest of list1 to the merged list.
        
        #I: 
        dummy = ListNode() 
        curr = dummy 

        while list1 and list2: 
            if list1.val <= list2.val: 
                curr.next = list1
                curr = curr.next 
                list1 = list1.next 
            else: 
                curr.next = list2
                curr = curr.next 
                list2 = list2.next 
        
        if list1: # list2 is null 
            curr.next = list1
        
        if list2: # list1 is null 
            curr.next = list2
        
        return dummy.next

        #R: list1: 1 -> 2 -> 4, list2: 1 -> 3 -> 5 -> 6
                    #         (l1)              (l2)
        # curr: dummy -> 1 (curr = list1 since list1.val <= list2.val and list1 ptr moves) -> 
        # 1 (curr.next = list2 since list1.val > list2.val and list 2 ptr moves) -> 2 -> 3 -> 4 -> 5 -> 6 
        # (5 -> 6 (rest of list2) is added once list1 is null)

        # dummy.next: 1 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6

        #E: Time: O(n), Space: O(1)
