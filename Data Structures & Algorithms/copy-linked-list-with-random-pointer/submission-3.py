class Solution:
    # Time: 10:58 - 12:20 
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #U: Create a deep copy of the LL and return head of the copied LL 

        #M/P: Use a hashmap to store the old nodes and its pointers 

        # After creating the hashmap, get the head of the deep copy with the hashmap 
        # Update the next and random pointers of each new node in the copied LL based on the 
        # next and random pointers of each original node. 

        #I: 

        if not head: 
            return None 

        hashmap = {None: None} 
        curr = head 

        # Creates the hashmap 
        while curr: 
            hashmap[curr] = Node(curr.val) # Next and Random are set to to none 
            curr = curr.next 
        
        curr = head 

        while curr: 
            newNode = hashmap[curr] #Accesses the original/copy node 
            newNode.next = hashmap[curr.next]
            newNode.random = hashmap[curr.random]
            curr = curr.next 

        return hashmap[head] #head of the copied list

        #Time: O(n), Space: O(n)