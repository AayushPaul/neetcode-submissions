class Solution:  
    # Time: 11:13 -   
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #U: Return sorted LL that is the result of merging all of the individual LL 

        #M/P: 

        #I:
        if not lists or len(lists) == 0: 
            return None  

        merged_list = lists[0]

        for i in range(1, len(lists)): 
            # lists[i] = sorted LL 

            merged_list = self.mergeLists(merged_list, lists[i])
        
        return merged_list 
    
    def mergeLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        dummy = ListNode(0) 
        curr = dummy 

        curr1, curr2 = list1, list2 

        while curr1 and curr2: 
            if curr1.val <= curr2.val: 
                curr.next = curr1
                curr = curr.next 
                curr1 = curr1.next 
            else: 
                curr.next = curr2
                curr = curr.next
                curr2 = curr2.next 
        
        if curr1: 
            curr.next = curr1
        
        if curr2: 
            curr.next = curr2 
        
        return dummy.next #head of the current merged LL
    
    #R: 1st iteration (list1: [1, 2, 4], list2: [1, 3, 5]): dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 5 = 1 -> 1 -> 2 -> 3 -> 4 -> 5
    #   2nd iteration (list1: 1 -> 1 -> 2 -> 3 -> 4 -> 5, list2: 3 -> 6): dummy.next = 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 5 -> 6

    #E: Time: O(n * m), Space: O(1)
