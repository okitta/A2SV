# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        start = head
        arr = []
        while start:
            arr.append(start.val)
            start = start.next

        def merg_sort(arr):
            if len(arr)>1:
                left = 0
                right = len(arr)
                mid = (left+right)//2
                left_arr = arr[:mid]
                right_arr = arr[mid:]


                merg_sort(left_arr)
                merg_sort(right_arr)

                left_idx = 0
                right_idx = 0
                merg_idx = 0
                while left_idx < len(left_arr) and right_idx < len(right_arr):
                    if left_arr[left_idx] < right_arr[right_idx]:
                        arr[merg_idx] = left_arr[left_idx]
                        left_idx += 1
                    else:
                        arr[merg_idx] = right_arr[right_idx]
                        right_idx += 1
                    merg_idx += 1
                while left_idx < len(left_arr):
                    arr[merg_idx] = left_arr[left_idx]
                    left_idx += 1
                    merg_idx += 1
                while right_idx < len(right_arr):
                    arr[merg_idx] = right_arr[right_idx]
                    right_idx += 1
                    merg_idx += 1
            return arr
        ans = merg_sort(arr)
        dummy = ListNode()
        dummy.next = head
        idx = 0
        while head:
            head.val = ans[idx]
            head = head.next
            idx += 1
        return dummy.next