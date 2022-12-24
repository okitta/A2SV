class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        pointer_num1 = m-1
        pointer_num2 = n-1
        
        for iterator in range( len(nums1)-1 , -1 , -1):
            if pointer_num2 < 0:
                break
            elif pointer_num1 < 0:
                nums1[iterator] = nums2[pointer_num2]
                pointer_num2 -=1
            elif  nums1[pointer_num1] < nums2[pointer_num2]: 
                nums1[iterator] = nums2[pointer_num2]
                pointer_num2 -= 1
            else:
                nums1[iterator] = nums1[pointer_num1]
                # nums1[pointer_num1] = nums2[pointer_num2]
                pointer_num1 -= 1
                
                
                