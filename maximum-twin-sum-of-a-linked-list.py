# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        array = []
        while head:
            array.append(head.val)
            head = head.next
        ans = [sum(i) for i in zip(array, array[::-1])]
        return max(ans)