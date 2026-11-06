"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #U: Create a deep copy of the list with n new nodes. 
            # The deep copy should consist of: original value of copied node, 
            # next pointer to the new node (next pointer of the original node), 
            # random pointer to new node (random pointer of the original node)

            # Each node is represented as a pair of [val, random_index] where 
            # random_index is index of the node (0-indexed) that random pointer 
            # points to, or null if it does not point to any node 

        #M/P: Two-Pass Approach with Hashmap 
        # Create a new head for copied version of LL 
        # Initialize curr pointer to start of the copied LL 
        # Use hashmap to store the values of the random pointers while going through the old LL (first pass)
        # Make the curr random pointer point to the stored value in the hashmap while going through the new LL (second pass)
        # Return LL with new head 

        #I: 
        if not head: 
            return None 
        
        # Purpose: Store old nodes to their new copies 
        hashmap = {}

        # First Pass: Creating all the new nodes and storing them in the hashmap
        curr = head 
        while curr: 
            hashmap[curr] = Node(curr.val)
            curr = curr.next 
        
        # Second Pass: Setting the next and random pointers of the new nodes to the correct nodes
        curr = head 
        newHead = hashmap[curr] 

        while curr: 
            #Gets new node from hashmap 
            newNode = hashmap[curr]
            newNode.next = hashmap.get(curr.next)
            newNode.random = hashmap.get(curr.random)
            curr = curr.next 

        return newHead 

        #E: Time: O(n), Space: O(n)