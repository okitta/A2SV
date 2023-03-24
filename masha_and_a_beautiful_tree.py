def solution():    
    test = int(input())
    
    
            
    for _ in range(test):
        counter = 0
        def merge(left,right):
            nonlocal counter
            arr = []
            if left[0] >= right[-1]:
                counter += 1
                arr.extend(right)
                arr.extend(left)
            else:
                arr.extend(left)
                arr.extend(right)
            return arr
        
        
        
        def mergeSort(left, right, arr):
            nonlocal counter
            if left == right:
                return [arr[left]]
            if left == right-1:
                if arr[left] > arr[right]:
                    counter += 1
                    return [arr[right],arr[left]]
                else:
                    return [arr[left],arr[right]]
            mid = (left + right) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
            return merge(left_half, right_half)
        
        size = int(input())
        array = list(map(int,input().split()))
        
        if sorted(array) == mergeSort(0,size-1,array):
            print(counter)
        else:
            print(-1)
solution()