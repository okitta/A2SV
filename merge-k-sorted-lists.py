# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        idx = 0
        dummy = ListNode()
        node = ListNode()
        dummy.next = node
        for row in lists:
            if row:
                heapq.heappush(heap,(row.val,idx))
            idx += 1
        if not heap:
            return dummy.next.next 
        while heap:
            item,idx = heapq.heappop(heap)
            node.val = item
            # if len(heap)>0:
            if lists[idx] and lists[idx].next:
                node.next = ListNode()
                node = node.next
                lists[idx] = lists[idx].next
                heappush(heap,(lists[idx].val,idx))
            elif len(heap)>0:
                node.next = ListNode()
                node = node.next
        return dummy.next