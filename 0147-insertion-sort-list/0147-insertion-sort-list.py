# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check = []
        start = head
        while start: 
            check.append(start.val)
            start = start.next
        start = head
        check.sort()
        for item in check:
            head.val = item
            head = head.next
        head = start
        return head
        