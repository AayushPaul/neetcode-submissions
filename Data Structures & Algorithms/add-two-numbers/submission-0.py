# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #U: Return the sum of the 2 numbers as a LL and digits are stored in reverse order

        #P: 
        # Create a dummy node 
        # Keep track of carries 
        # While l1 or l2 or carry 
            # Determine new node value and new carry value 
            # add new nodes with new node values to LL 
            # On each iteration, check if nodes in l1 or l2 exist 
                # Move l1 or l2 pointers then 

        #I: 
        dummy = ListNode(0) 
        curr = dummy 
        carry = 0 
        
        while l1 or l2 or carry: 
            if l1: 
                val1 = l1.val
            else: 
                val1 = 0 
            
            if l2: 
                val2 = l2.val 
            else: 
                val2 = 0
            
            val = val1 + val2 + carry #val = 16
            carry = val // 10   # 1 will be carried 
            val = val % 10 # Actual new node value in the final LL (6) 
            curr.next = ListNode(val) #Points to the new node with new value
            curr = curr.next 

            if l1: 
                l1 = l1.next 
            
            if l2: 
                l2 = l2.next 
            
        return dummy.next 

        #E: Time: O(M + N), Space: O(1)
        