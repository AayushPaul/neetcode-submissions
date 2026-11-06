# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #U: Return true if there is a cycle in LL. Otherwise, return False. 

        #M/P: Slow and Fast Pointers 

        #I: 
        slow, fast = head, head 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next #Moves twice as fast 

            if slow == fast: 
                return True 
            
        return False
        
        #R: 
            # head = 1 -> 2 -> 3 -> 4
                # slow, fast = head, head 
            
        #E: Time: O(n), Space: O(1)
