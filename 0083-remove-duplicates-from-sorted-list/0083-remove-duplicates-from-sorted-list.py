class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        
        if head and not head.next:
            dummy.next = head
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            temp.next = head
            temp = temp.next
            head = head.next
        return dummy.next