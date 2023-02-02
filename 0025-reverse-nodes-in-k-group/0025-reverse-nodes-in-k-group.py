# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        length = 0
        while start:
            start = start.next
            length += 1
        link = []
        while head:
            group = k
            previous = None
            current = head
            last = head
            if length < k:
                link.append([last])
                break
            while group > 0 and length >= k:
                group -= 1
                after = current.next
                current.next = previous
                previous = current
                current = after
            length -= k
            link.append([previous,last])
            head = current
        for index in range(len(link)-1):
            start = link[index][1]
            nxhead = link[index+1][0]
            start.next = nxhead
            # while start.next:
            #     start = start.next
            # start.next = link[index + 1]
                
        return link[0][0]
            
            
