# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Time: 12:26 - 12:32 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #U: Return true if there is a cycle in the LL. Otherwise, return False. 
            # There is a cycle in LL if at least one node in the list can be visited again 
            # by following the next pointer. 

        #M/P: Fast and slow pointer method 

        #I: 
        slow, fast = head, head 
        
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast: 
                return True 
        
        return False

        #E: Time: O(n), Space: O(1) 