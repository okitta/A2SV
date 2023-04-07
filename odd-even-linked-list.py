# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None or head.next.next == None:
            return head
        
        odd,even = head, head.next
        pointer1,pointer2 = odd,even
        prev = None
        while(pointer1 != None and pointer2 != None):
            pointer1.next = pointer2.next
            prev = pointer1
            pointer1 = pointer1.next
            if pointer1 == None:
                pointer2.next = None
            else:
                pointer2.next = pointer1.next
            pointer2 = pointer2.next
        if pointer1 == None:
            prev.next = even
        else:
            pointer1.next = even
        return odd