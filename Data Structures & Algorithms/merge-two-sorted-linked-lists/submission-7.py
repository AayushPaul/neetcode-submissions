class Solution:
    # Time: 1:16 - 1:40 
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #U: Merge the 2 lists into one sorted LL and return head of the new sorted LL 
            # The new list should be made up of nodes from list1 and list2

        #M/P: 
            # Create a dummy node, and connect that node to node with lowest value (either from list1 or list2)

        #I: 
        dummy = ListNode()
        temp = dummy 

        while list1 and list2: 
            if list1.val < list2.val: 
                temp.next = list1
                temp = temp.next 
                list1 = list1.next 
            else: 
                temp.next = list2
                temp = temp.next 
                list2 = list2.next

        temp.next = list1 if list1 else list2
        return dummy.next 

        #R: 
            # list1 = 1 -> 2 -> 4, list2 = 1 -> 3 -> 5
            # 1 -> 1 -> 2 -> 3 -> 4 -> 5
        
        #E: Time: O(n + m), Space: O(1)