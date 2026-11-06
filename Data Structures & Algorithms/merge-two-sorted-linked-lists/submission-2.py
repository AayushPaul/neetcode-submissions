# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #U: Merge the two lists into one sorted LL and return the head of the new LL 

        #M/P: 
            # Initialize dummy node and make tail node equal to dummy node 
            # While loop that checks if list1 and list2 are NOT null 
                # Compare the node values across both lists and move the tail pointer based on those comparisons 
            
            # if list1 is null, make the rest of the merged list filled with remaining list2 nodes 
            # if list2 is null, make the rest of the merged list filled with remaining list1 nodes

            # return dummy.next 

        #I: 
        dummy = ListNode() 
        tail = dummy 
        
        while list1 and list2: 
            if list1.val <= list2.val: 
                tail.next = list1
                list1 = list1.next 
            else: 
                tail.next = list2
                list2 = list2.next 

            tail = tail.next 

        if not list1: 
            tail.next = list2
        
        if not list2: 
            tail.next = list1 

        return dummy.next 

        #R: 
            #list1 = [1, 2, 4], list2 = [1, 3, 5]
            # Note: tail is the main pointer of the merged list 
            # dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 5 
            # (the first node in this merged list is dummy.next because tail = dummy at beginning and tail is main ptr that moves)

            # final: 1 -> 1 -> 2 -> 3 -> 4 -> 5 

        #E: Time: O(n), Space: O(1) 