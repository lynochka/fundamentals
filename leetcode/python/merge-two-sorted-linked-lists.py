# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None or list2 is None:
            return list1 or list2
        
        current1 = list1
        current2 = list2
        
        head = ListNode()
        last_node = None

        while current1 is not None and current2 is not None:
            if current1.val <= current2.val:
                next_node = ListNode(val=current1.val)
                current1 = current1.next
            else:
                next_node = ListNode(val=current2.val)
                current2 = current2.next
            
            if last_node == None:
                head.next = next_node 
            else:
                last_node.next = next_node
            last_node = next_node             

        if current1 is not None:
            last_node.next = current1

        if current2 is not None:
            last_node.next = current2 

        return head.next