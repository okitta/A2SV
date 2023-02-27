class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_window_size = 1
        start = 0
        idx = 0
        if len(arr) == 2 and arr[0] != arr[1]:
            return 2
        for idx in range(1,len(arr)-1):
            if arr[idx-1] == arr[idx] == arr[idx+1]:
                start = idx
            elif  not (arr[idx-1] < arr[idx] > arr[idx+1] or arr[idx-1] > arr[idx] < arr[idx+1]):
                max_window_size = max(max_window_size,idx - start + 1)
                start = idx
        if start < idx-1:
            return max(max_window_size,idx-start+2)
        else:
            return max_window_size
                
            
        
#         start = left = 0
#         right = 1
#         index = []
#         if len(arr) <= 1:
#             return 1
        
#         for idx in range(1,len(arr)):
#             if arr[idx-1] > arr[idx]:
#                 index.append(1)
#             elif arr[idx-1] < arr[idx]:
#                 index.append(-1)
#             else:
#                 index.append(0)
                
#         if len(index) == 1 and index[0]:
#             return 2
#         while right < len(index):
#             if index[left] != 0 or index[right] != 0:
#                 if index[right] == -index[left]:
#                     right += 1
#                     left += 1
#                 else:
#                     max_window_size = max(max_window_size,right-start+1)
#                     start = right
#                     left = right
#                     right += 1

#             else:
#                 start = right
#                 left = right
#                 right += 1
#         if start < left:
#             return max(max_window_size,right-start+1)
#         else:
#             return max_window_size

