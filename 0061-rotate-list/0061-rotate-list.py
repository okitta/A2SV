# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        length = 0
        while head:
            head = head.next
            length += 1
        # print(length)
        head = start
        while k>length:
            if not head:
                return head
            k = k%length
        # print(k)
        for i in range(k):
            temp = head.val
            while head:
                head.val , temp = temp , head.val
                head = head.next
            start.val = temp
            head= start
        return start
                    
                
                
        