class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = temp2 = head
        count = 0

        while temp:
            count += 1
            temp = temp.next
        if count == n:
            return head.next
        for x in range(count-n-1):
            temp2 = temp2.next
        if temp2.next:
            temp2.next = temp2.next.next
        elif temp2:
            temp2.next = None

        return head
