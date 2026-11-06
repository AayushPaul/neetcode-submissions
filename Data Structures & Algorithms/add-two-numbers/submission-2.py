# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #U: Return the sum of the 2 numbers as a LL and digits are stored in reverse order

        #M/P: Have a curr pointer for the final sumLL 
            # 

        #I:  
        dummy = ListNode() 
        curr = dummy 
        carry = 0 

        while l1 or l2 or carry: 
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0 

            val = v1 + v2 + carry 
            carry = val // 10
            val = val % 10 
            curr.next = ListNode(val) 

            # Update ptrs 
            curr = curr.next 
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 
        
        return dummy.next 

        #R: 
            # l1: 7 -> 2 -> 0
            # l2: 8 -> 2 -> 3

        # dummy -> 5 -> 7 -> 9 -> 4 -> 5

                     #  (1)
            # (LL): 7 -> 2 -> 0 -> 1
               #  + 8 -> 2 -> 3 -> 0
               # ------
        # dummy ->  5 -> 5 -> 3 -> 1
        # 5 -> 5 -> 3 -> 1

            # 328 + 1027 = 1355