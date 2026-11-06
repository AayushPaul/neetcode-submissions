# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #11:15 - 12:04
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #U: Remove the nth node from the end of the list and return the beginning of the list

        #M/P: 
            # Think about edge cases: n = 0 or n = 1

            # Multiple pass approach
                # In the first pass, the program can iterate through the LL and determine 
                # the length of the LL 

                # After the first pass, we determine the index of the LL at which we have to remove 
                # that element: index = length of LL - n 
                    # head = [1, 2, 3, 4], n = 2 
                        # len(head) = 4, index = 4 - n = 4 - 2 = 2; 3 is removed from the LL 
                
                # In the 2nd pass, on each iteration of a while loop, we can increment the index value 
                # until index value is equal to the index value we are trying to get. When that happens, 
                # we remove the node at the index value using LL ops (curr = curr.next.next)

                # Return head 
        
        #I: 
        curr = head 
        length, index = 0, 0 

        # The first pass 
        while curr: 
            length += 1
            curr = curr.next 

        # The second pass 
        secondCurr = head   
        correctIndex = length - n 

        #Edge Case 
        if correctIndex == 0: 
            return head.next 

        while secondCurr: 
            if index == correctIndex - 1: 
                secondCurr.next = secondCurr.next.next #Output: 1 -> 2 -> 3 -> 4
                break
            
            secondCurr = secondCurr.next 
            index += 1

            #correctIndex = 2, index = 2, 1 -> 2 -> 4
        
        return head 

    # Time: O(2n) simplified to O(n), Space: O(1)