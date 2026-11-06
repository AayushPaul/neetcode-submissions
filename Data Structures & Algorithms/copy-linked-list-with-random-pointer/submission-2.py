"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # Time: 10:58 - 
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #U: Create a deep copy of the LL and return head of the copied LL 

        #M/P: Use a hashmap to store the old nodes and its pointers 

        # After creating the hashmap, get the head of the deep copy with the hashmap 
        # Update the next and random pointers of each new node in the copied LL based on the 
        # next and random pointers of each original node. 

        #I: 

        if not head: 
            return None 
            
        hashmap = {} 
        curr = head 

        # Creates the hashmap 
        while curr: 
            hashmap[curr] = Node(curr.val) # Next and Random are set to to none 
            curr = curr.next 
        
        curr = head 

        while curr: 
            newNode = hashmap[curr] #Accesses the original node 
            newNode.next = hashmap.get(curr.next)
            newNode.random = hashmap.get(curr.random)
            curr = curr.next 

        return hashmap[head]

        #R: Original LL: 3 -> 7 -> 4 -> 5 -> null 
            # [3, null], [7, 3], [4, 0], [5, 1] (2nd num is the random ptr)

            # Final ans: 3 -> 7 -> 4 -> 5 -> null (hashmap[head]) 

        #E: Time: O(n), Space: O(n) 