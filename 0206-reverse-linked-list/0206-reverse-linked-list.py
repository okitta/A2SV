# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        """
        1,2,3,4,5
              p c t
        """
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre