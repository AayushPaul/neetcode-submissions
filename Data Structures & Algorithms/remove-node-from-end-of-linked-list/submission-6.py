class Solution:
    #6:48 - 8:00 
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #U: Remove the nth node from end of the list and return the start of the list 

        #M/P: Initialize dummy node, index, curr, and prev vars 
        # First while loop goes through the LL and counts the number of nodes; the # nodes is the length of the LL 

        # Second while loop goes through the LL with an index variable 
            # On each iteration, when len(LL) - index == n, make the next pointer of prev node point to the next 
            # node in LL, which removes the current node  

        # Return dummy.next 

        #I: 
        curr, length = head, 0
        while curr: 
            length += 1
            curr = curr.next 
        
        newCurr = head 
        dummy = ListNode(0, head)
        prev = dummy 
        index = 0

        while newCurr: 
            if length - index == n: 
                prev.next = newCurr.next 
                break
            else:
                index += 1
                prev = newCurr
                newCurr = newCurr.next
        
        return dummy.next

        #E: Time: O(n), Space: O(1) 