class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        pointer = 1
        for index in range(len(arr)-1):
            if arr[index] > arr[pointer]:
                return False
            else:
                pointer += 1
        return True

#{ 