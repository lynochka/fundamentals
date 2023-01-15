# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 0
        fake_head = ListNode(next=head)
        node = fake_head
        prior_to_remove_node = fake_head
        
        while node.next:

            if count > n-1:
                prior_to_remove_node = prior_to_remove_node.next
            node = node.next
            count += 1
        
        remove_node = prior_to_remove_node.next
        prior_to_remove_node.next = remove_node.next

        return fake_head.next