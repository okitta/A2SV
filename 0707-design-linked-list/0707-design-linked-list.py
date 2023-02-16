class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        cur = self.head
        
        for _ in range(0, index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        cur = self.head
        new_node = ListNode(val)

        if index <= 0:
            new_node.next = cur
            self.head = new_node
        else:
            for _ in range(index - 1):
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        cur = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                cur = cur.next
            cur.next = cur.next.next

        self.length -= 1