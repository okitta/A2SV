# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        for i in range(1, left):
            pre = pre.next

        start = pre.next
        cur = start.next
        for i in range(left, right):
            start.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = start.next
        
        return dummy.next