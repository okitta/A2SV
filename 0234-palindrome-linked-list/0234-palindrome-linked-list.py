# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        check_list = []
        while head:
            check_list.append(head.val)
            head= head.next
        right_pointer = len(check_list) - 1
        left_pointer = 0
        while left_pointer <= right_pointer:
            if check_list[left_pointer] != check_list[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        return True
        
        