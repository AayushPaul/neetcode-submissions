# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Time: 12:26 - 12:32 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #U: If there is a cycle, return True. If not, return False 

        #M/P: Fast and Slow Pointer Method 

        #I: 
        slow, fast = head, head 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast: 
                return True 
        
        return False 

        #E: Time: O(n), Space: O(1) 