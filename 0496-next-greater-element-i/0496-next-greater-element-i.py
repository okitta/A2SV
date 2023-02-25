class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        hash_dict = defaultdict(lambda:-1)
        for num in nums2:
            while ans and ans[-1] < num:
                hash_dict[ans[-1]] = num
                ans.pop()
            ans.append(num)
        return [hash_dict[num] for num in nums1]
                
        