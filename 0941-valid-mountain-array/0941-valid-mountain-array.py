class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) >=3 :
            
            max_index = arr.index(max(arr))
            
            if max_index!=0 and max_index!=len(arr)-1:
                
                left = arr[:max_index]
                left_s = sorted(left)

                right = arr[max_index:]
                right_s = sorted(right,reverse=True)

                R_A = len(right_s)
                R_B = len(set(right))
                L_A = len(left_s)
                L_B = len(set(left))

                if left_s == left and L_A == L_B and right_s == right and R_A == R_B:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False