# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None or list2 is None:
            return list1 or list2
        
        head = last_node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                last_node.next = list1
                list1 = list1.next
            else:
                last_node.next = list2
                list2 = list2.next
            
            last_node = last_node.next   

        if list1:
            last_node.next = list1

        if list2:
            last_node.next = list2 

        return head.next