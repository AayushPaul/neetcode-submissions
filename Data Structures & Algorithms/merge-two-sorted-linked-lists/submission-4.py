class Solution:
    # Time: 11:00 - 
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #U: Merge the 2 lists into one sorted LL and return head of the new sorted LL 

        #M/P: 
            # If curr1.val <= curr2.val: 
                # 

        #I: 
        dummy = ListNode() 
        mainPtr = dummy 
        curr1, curr2 = list1, list2

        while curr1 and curr2: 
            if curr1.val <= curr2.val: 
                mainPtr.next = curr1
                mainPtr = curr1
                curr1 = curr1.next
            else: 
                mainPtr.next = curr2
                mainPtr = curr2
                curr2 = curr2.next 

        if not curr1: 
            mainPtr.next = curr2
        elif not curr2: 
            mainPtr.next = curr1

        return dummy.next

        #R: 

        #E: Time: O(n + m), Space: O(1) 