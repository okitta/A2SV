#User function Template for python3

class Solution:
    def subsets(self, A):
        #code here
        ans = [[]]
        def backtrack(arr,curr):
            if len(arr) > 0:
                ans.append(arr[::])
            for i in range(curr,len(A)):
                arr.append(A[i])
                backtrack(arr,i+1)
                arr.pop()
        backtrack([],0)
        ans.sort()
        return ans
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        A = list(map(int,input().strip().split()))
        
        ob=Solution()
        result =ob.subsets(A)
        
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j],end=" ")
                
            print()
            
            

# } Driver Code Ends