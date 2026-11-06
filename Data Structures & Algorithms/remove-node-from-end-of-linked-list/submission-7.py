class Solution:
    #12:55 - 1:41 
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #U: Given head of LL and integer n, remove nth node from end of LL and return its head. 

        #M/P: 

        #I: 
        curr = head 
        length = 1
        while curr.next: 
            curr = curr.next
            length += 1
        
        targetIdx = length - n 
        
        count = 0
        dummy = ListNode(0) 
        dummy.next = head 
        prev = dummy 
        curr = head 

        while curr: 
            if count == targetIdx: 
                prev.next = curr.next 
                break
            else: 
                prev = prev.next
                curr = curr.next
            
            count += 1
        
        return dummy.next