class Solution: 
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            min_index = i
            for j in range(min_index+1,n):
                if arr[j] < arr[min_index]:
                    min_index = j
            if i != min_index:
                arr[i] , arr[min_index] = arr[min_index] , arr[i]