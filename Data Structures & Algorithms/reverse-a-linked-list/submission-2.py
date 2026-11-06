# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #U: Reverse the list 
        
        #M: Singly LL with pointers 

        #P: 
            #1. Set two pointers: prev = None, current = head 
            #2. while current exists: 
                #3. Set a variable called next = current.next 
                #4. prev = current 
                #5. current.next = prev 
                #6. current = next 
        
        #I: 
        #Main lesson: Always set pointers before changing the nodes 
        prev, current = None, head

        while current: 
            nxt = current.next  
            current.next = prev
            prev = current
            current = nxt
        
        return prev #New head of LL

        #R: Example 1/2

        #E: Time: O(n), Space: O(1)